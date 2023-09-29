import re
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
import asyncio
import aiohttp
import time

headers={
                    'User-Agent': "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
}



async def main(urls,startnum,ix):
    async with aiohttp.ClientSession(trust_env=True) as session:
        ret = await asyncio.gather(*[get(url,session,startnum+i,ix) for i,url in enumerate(urls)])
        print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))
        return ret
async def get(url, session,startnum,i):
    #print(url)
    try:
        async with session.get(url=url,headers=headers,timeout=12) as response:
            resp = await response.read()
            print("{}: Successfully got url {} with resp of length {}.".format(startnum,url, len(resp)))
            if(resp is not None):
                #print(resp)
                try:
                    soup = BeautifulSoup(resp,'lxml')
                    data = soup.find_all('script',attrs={ "data-hypernova-key" :"yelpfrontend__5460__yelpfrontend__GondolaSearch__dynamic" })#  attrs={ "data-hypernova-key" :"yelpfrontend__54515__yelpfrontend__GondolaSearch__dynamic" }
                    datastr = data[0].getText()[4:-4]
                    arridx=[m.start() for m in re.finditer('{"ranking":', datastr)]
                    arridy=[m.start() for m in re.finditer(',"scrollablePhotos":', datastr)]
                    loaded = []
                    #print(datastr)
                    for z in range(10):
                        loaded.append(json.loads(datastr[arridx[z]:arridy[z]]))
                        #print(json.loads(datastr[arridx[z]:arridy[z]]))

                        if loaded[z]['website'] is not None:
                            loaded[z]['website']=loaded[z]['website']['href']
                            # print(loaded[z]['website'])
                    df = pd.DataFrame(loaded)
                    return df
                    # df.to_csv("data.csv",mode='a')        
                except:
                    i.write(url+'\n')
                    pass

    except Exception as e:
        try:
            print("{}: Unable to get url {} due to {}.".format(startnum,url, e.__class__))
            i.write(url+'\n')
        #        errors.add(url)
            return None
        except:
            print("error")
def chonk(arrdata,chonksize):
    chonk = []
    chonkytonk = []
    count = 0
    for x in arrdata:
        chonk.append(x)
        #print(x)
        if count>chonksize:
            count = 0
            chonkytonk.append(chonk)
            chonk = []
        count = count +1
    return chonkytonk

def y():

    # btype = ["bakeries","cafe"]
    # baseurl = 'https://www.yelp.com/search?find_desc='
    # locurl = '&find_loc='
    # #https://www.yelp.com/search?find_desc=cafe&find_loc=toyko+japan
    # start_urls=[]
    # start_index = 0

    # for i in range(len(cities)):
    #     for b in btype:
    #         start_urls.append(baseurl+str(b)+str(locurl)+cities[i])
    #         for c in range(1,24):
    #             start_urls.append(baseurl+str(b)+str(locurl)+str(cities[i])+"&start="+str(c*10))
    #start_urls = start_urls[0:4]

    # chonk = []
    # chonkytonk = []
    # chonksize = 10
    # count = 0
    # for x in start_urls:
    #     chonk.append(x)
    #     #print(x)
    #     if count>chonksize:
    #         count = 0
    #         chonkytonk.append(chonk)
    #         chonk = []
    #     count = count +1
    startfile = 210
    endfile = 214
    startindex = 3185
    chonksize = 7
    for x in range(startfile,endfile):
        f = open("city-"+str(x)+".txt","r",encoding="utf-8")
        start_urls = f.read().split("\n")
        f.close()
        start_urls = start_urls[startindex:]
        chonkytonk = chonk(start_urls,chonksize)
        #print(chonkytonk)
        for chunk in chonkytonk:
            # g = open("testing.txt","a",encoding='utf')
            # g.write('\n'.join(chunk)+"\n")
            # g.close()
            i = open("yelp_error.txt","a",encoding="utf-8")
            df = asyncio.run(main(chunk,startindex,i))
            i.close()
            try:
                for y in df:
                    print(x)
                    y.to_csv("data-"+str(x)+".csv",mode='a',header=None,index=False)
            except:
                pass
            time.sleep(4)
            del df
            # print(chunk)
            startindex = startindex+chonksize+1
        startindex = 0

y()
