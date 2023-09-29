#import requests
from logging import exception
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import asyncio
import aiohttp
from aiohttp import ClientSession
import time
import re
import os ##mkdir 
import gc
import threading


headers={
                    'User-Agent': "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
}
initial = [] 
pages = []
links = []
emails = []
links2 = []
txtfile = "webmil-"
ext = ".txt"
emailtxt = "-email.txt"
linktxt = "-link.txt"
errortxt = "-error.txt"

loopcount = 0
# async def parse(htmls,countnum):
#     for x in htmls:
#         if(x is not None):
#             try:
#                 tempemail = extractEmail(x[1])
#                 g = open("q"+txtfile+str(countnum)+emailtxt,"a",encoding="utf-8")
#                 g.write('\n'.join(tempemail)+'\n')
#                 g.close()
#                 del tempemail
#             except:
#                 pass
#             links2temp = get_linked_urls(x[0],x[1])
#             h = open("q"+txtfile+str(countnum)+linktxt,"a",encoding="utf-8")
#             h.write('\n'.join(links2temp)+'\n')
#             h.close()
#             del links2temp
#         gc.collect()

async def get(url, session,startnum,g,h,i):
    #print(url)
    try:
        async with session.get(url=url,headers=headers,timeout=12) as response:
            resp = await response.read()
            print("{}: Successfully got url {} with resp of length {}.".format(startnum,url, len(resp)))
            if(resp is not None):
                try:
                    tempemail = extractEmail(resp)
                    # g = open("q"+txtfile+str(countnum)+emailtxt,"a",encoding="utf-8")
                    g.write('\n'.join(tempemail)+'\n')
                    links2temp = get_linked_urls(url,resp)
                    h.write('\n'.join(links2temp)+'\n') 
                    # g.close()
                    # del tempemail
                except:
                    i.write(url+'\n')
                    pass
                     
                # h = open("q"+txtfile+str(countnum)+linktxt,"a",encoding="utf-8")
                # h.close()
                # del links2temp
            gc.collect()
    except Exception as e:
        try:
            print("{}: Unable to get url {} due to {}.".format(startnum,url, e.__class__))
            i.write(url+'\n')
        #        errors.add(url)
            return None
        except:
            print("error")
            
# async def get(url, session):
#     #print(url)
#     try:
#         async with session.get(url=url,headers=headers,timeout=8) as response:
#             resp = await response.read()
#             print("Successfully got url {} with resp of length {}.".format(url, len(resp)))
#             return(url,resp)
#     except Exception as e:
#         try:
#             print("Unable to get url {} due to {}.".format(url, e.__class__))
#             h = open(txtfile+str(loopcount)+ext,"a",encoding="utf-8")
#             h.write("Unable to get url {} due to {}.\n".format(url, e.__class__))
#             h.close()
#         #        errors.add(url)
#             return None
#         except:
#             print("error")
            
# async def get2(url, session):
#     print(url)
#     try:
#         async with session.get(url=url,headers=headers,timeout=42) as response:
#             resp = await response.read()
#             print("Successfully got url {} with resp of length {}.".format(url, len(resp)))
#             links2temp = get_linked_urls(resp)
#             emailstemp = extractEmail(url,resp)
#             g=open(txtfile+str(loopcount)+emailtxt,"a",encoding="utf-8")
#             g.write('\n'.join(emailstemp))
#             g.close()
#             h=open(txtfile+str(loopcount)+linktxt,"a",encoding="utf-8")
#             h.write('\n'.join(links2temp))
#             h.close()
#             return links2temp
# #            
#     except Exception as e:
#         print("Unable to get url {} due to {}.".format(url, e.__class__))
# #        errors.add(url)
#         return None


async def main(urls,startnum,g,h,i):
    async with aiohttp.ClientSession(trust_env=True) as session:
        ret = await asyncio.gather(*[get(url,session,startnum+i,g,h,i) for i,url in enumerate(urls)])
        print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))
        return ret
"""    
async def main2(urls):
    async with aiohttp.ClientSession() as session:
        #ret = await asyncio.gather(*[get2(url, session) for url in urls])
        for url in urls:
            asyncio.run(get2(url,session))
            print("ASFDASDDFAS",url,"ASDFASFASDFASDFASDFADS")
        print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))
        return ret

"""


def extractEmail(bytes):
    #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    html = str(bytes, encoding='utf-8')
    emaillist = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', html)
#            emails = re.findall(r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$',html)
    #print(emaillist)
    return emaillist
   
    """for email in emaillist:
        if (email not in emails):
            count += 1
            print(email)
            listUrl.append(email)
         """   
    print("")
    print("***********************")
    print( count,"emails were found")
    print("***********************")



#    except KeyboardInterrupt:
#        pass

#    except Exception as e:
#        pass

#    return listUrl
"""
def get_linked_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        try:
            path = link.get('href')
            #print(soup.find_all('a','href'))
            if path and path.startswith('/'):
                path = urljoin(url, path)
                yield path
#            if len(url)>0:    
 #               if url[12:] in path:
  #                  #print(True)
   #                 yield path
        except:
            pass
"""

def get_linked_urls(url, bytes):
    html = bytes.decode('utf8', errors='replace')

    arrlink =[]
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        try:
            path = link.get('href')
                #print(soup.find_all('a','href'))
            if path and path.startswith('/'):
                path = urljoin(url, path)
                #yield path
                arrlink.append(path)
            if len(url)>0:    
                if url[12:] in path:
                    #print(True)
                    #yield path
                    arrlink.append(path)
        #if path.startswith("mailto:"):
            #g.write(url)
        except:
            pass
    return arrlink
def chonky(countnum):
    f = open(txtfile+str(countnum)+ext,"r")
    initial = f.read().split('\n')
    chonk = []
    chonkytonk = []
    linkx =[]
    f.close()
    chonksize = 42
    count = 0
    for x in initial:
        chonk.append(x)
        #print(x)
        if count>chonksize:
            count = 0
            chonkytonk.append(chonk)
            chonk = []
        count = count +1

    for chunk in chonkytonk:
        linkx = asyncio.run(main(chunk))
        links2 = []
        for x in linkx:
            #print(len(2))
            try:
                tempemail = extractEmail(x[1])
                g = open("email.txt","a",encoding='utf-8')
                h = open("q"+txtfile+str(loopcount)+emailtxt,"a",encoding="utf-8")
                g.write('\n'.join(tempemail))
                g.close()
            except:
                pass
            #try:
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            if(x is not None):
                links2temp = get_linked_urls(x[0],x[1])
                links2 = links2 + links2temp
                #print(links2)
                h = open("q"+txtfile+str(loopcount)+linktxt,"a",encoding="utf-8")
              #  h = open("link.txt","a",encoding='utf-8')
                h.write('\n'.join(links2temp))
                h.close()
            #except:
                #pass
              #  print("errorYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
        time.sleep(.4)
    link2l = {''}
    qf = open("q"+txtfile+str(loopcount)+linktxt,"r",encoding="utf-8")
    for y in links2:
        link2l.add(y)
    for y in link2l:
        chonk.append(y)
        if count>chonksize:
            count = 0
            chonkytonk.append(chonk)
            chonk = []
        count = count +1

    for chunk in chonkytonk:
        linky = asyncio.run(main(chunk))
        for y in linky:
            try:
                tempemail = extractEmail(y[1])
                g = open("d"+txtfile+str(loopcount)+emailtxt,"a",encoding="utf-8")
                g.write('\n'.join(tempemail))
                g.close()
            except:
                pass
            if y is not None:
                links2temp = get_linked_urls(y[0],y[1])
                links2 = links2 + links2temp
                h = open("d"+txtfile+str(loopcount)+linktxt,"a",encoding="utf-8")
   #             h = open("link.txt","a",encoding='utf-8')
                h.write('\n'.join(links2temp))
                h.close()
        time.sleep(.4)
        return links2



def q(countnum,start,ds,cs):
    f = open(txtfile+str(countnum)+ext,"r")
    initial = f.read().split('\n')
    initial = initial[start:]
    chonk = []
    chonkytonk = []
    linkx =[]
    f.close()
    chonksize = cs
    count = 0
    for x in initial:
        chonk.append(x)
        #print(x)
        if count>chonksize:
            count = 0
            chonkytonk.append(chonk)
            chonk = []
        count = count +1

    for chunk in chonkytonk:
        
        g = open("q"+txtfile+str(countnum)+emailtxt,"a",encoding="utf-8")
        h = open("q"+txtfile+str(countnum)+linktxt,"a",encoding="utf-8")
        i = open("q"+txtfile+str(countnum)+errortxt,"a",encoding="utf-8")

        linkx = asyncio.run(main(chunk,start,g,h,i))
        #asyncio.run(parse(linkx,countnum,g,h))
        g.close()
        h.close()
        i.close()
        del linkx
        # threadx = threading.Thread(target = parse(linkx,countnum))
        # threads = list()
        # threads.append(x)
        # x.start()



        # #links2 = []
        # for x in linkx:
        #     if(x is not None):
        #     #print(len(2))
        #         try:
        #             tempemail = extractEmail(x[1])
        #             #g = open("email.txt","a",encoding='utf-8')
        #             #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #             #print("q"+txtfile+str(countnum)+emailtxt,"a")
        #             g = open("q"+txtfile+str(countnum)+emailtxt,"a",encoding="utf-8")
        #             #print("XXXXXXXXXXYYYYYYYYYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        #             g.write('\n'.join(tempemail)+'\n')
        #            #print("YYYYYYYYYYYYYYYYYYYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        #             g.close()
        #             del tempemail
        #         except:
        #             pass
        #         #try:
        #         #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #         links2temp = get_linked_urls(x[0],x[1])
        #         #links2 = links2 + links2temp
        #         #print(links2)
        #         h = open("q"+txtfile+str(countnum)+linktxt,"a",encoding="utf-8")
        #       #  h = open("link.txt","a",encoding='utf-8')
        #         h.write('\n'.join(links2temp)+'\n')
        #         h.close()
        #         del links2temp
        #     #except:
        #         #pass
        #       #  print("errorYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
        # del linkx  
        gc.collect()
        start = start + cs-1
        time.sleep(ds)
def d(countnum,ds,cs):
    link2l = {''}
    qf = open("q"+txtfile+str(countnum)+linktxt,"r",encoding="utf-8")
    initial = qf.read().split('\n')
    chonk = []
    chonkytonk = []
    qf.close()
    chonksize = cs
    count = 0
    for y in initial:
        link2l.add(y)
    for y in link2l:
        chonk.append(y)
        if count>chonksize:
            count = 0
            chonkytonk.append(chonk)
            chonk = []
        count = count +1

    for chunk in chonkytonk:
        linky = asyncio.run(main(chunk))
        for y in linky:
            if(x is not None):
                try:
                    tempemail = extractEmail(y[1])
                    g = open("d"+txtfile+str(countnum)+emailtxt,"a",encoding="utf-8")
                    g.write('\n'.join(tempemail)+'\n')
                    g.close()
                except:
                    pass
                if y is not None:
                    links2temp = get_linked_urls(y[0],y[1])
                    #links2 = links2 + links2temp
                    h = open("d"+txtfile+str(countnum)+linktxt,"a",encoding="utf-8")
    #             h = open("link.txt","a",encoding='utf-8')
                    h.write('\n'.join(links2temp)+'\n')
                    h.close()
        time.sleep(ds)



startnum = 0
for x in range(46,75):
    loopcount = x
    q(x,startnum,4,222)
    startnum = 0