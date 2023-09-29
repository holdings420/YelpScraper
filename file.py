
# """
# for x in range(len(data)):
#     if 'esu.com.ua' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if 'web.archive' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if 'google' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if 'youtube' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.png' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.jpeg' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.jpg' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if 'wixpress' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '%' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.webp' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.gif' in data[x]:
#         rm.append(x)
#         #print(data[x])        
#     if 'sentry.io' in data[x]:
#         rm.append(x)
#         #print(data[x])        
#     if '.avif' in data[x]:
#         rm.append(x)
#         #print(data[x])     
#     if 'redbubble' in data[x]:
#         rm.append(x)
#         #print(data[x])     
# for x in reversed(range(len(rm))):
#     print(data[rm[x]])
#     print(len(data),x,rm[x])
#     data.pop(rm[x])
# datalist = {''}
# for x in data:
#     datalist.add(x)
# f.close()

# g = open("email-0-0.txt","w")
# g.write('\n'.join(datalist))
# g.close()
# """


# #f = open("emailwebsite-1.txt","r")
# #data = f.read().split('\n')
# #rm  = []


#     """
#     if 'esu.com.ua' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if 'web.archive' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if 'google' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if 'youtube' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.png' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.jpeg' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.jpg' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if 'wixpress' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '%' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.webp' in data[x]:
#         rm.append(x)
#         #print(data[x])
#     if '.gif' in data[x]:
#         rm.append(x)
#         #print(data[x])        
#     if 'sentry' in data[x]:
#         rm.append(x)
#         #print(data[x])        
#     if '.avif' in data[x]:
#         rm.append(x)
#         #print(data[x])     
#     if 'redbubble' in data[x]:
#         rm.append(x)
#         #print(data[x])     
#     if 'xmpp.' in data[x]:
#         rm.append(x)
#         #print(data[x]) 
#     if '.webm' in data[x]:
#         rm.append(x)
#     if 'body.content@' in data[x]:
#         rm.append(x)
#     if 'room@groups.camp' in data[x]:
#         rm.append(x)
#     if '.js' in data[x]:
#         rm.append(x)
#     if '.svg' in data[x]:
#         rm.append(x)
#     if '.wiki' in data[x]:
#         rm.append(x)
#     if 'name' in data[x]:
#         rm.append(x)
#     if 'example' in data[x]:
#         rm.append(x)
#     if '.mp' in data[x]:
#         rm.append(x)

#     """
num = 24


f = open("qbake-"+str(num)+"-email.txt","r")
data = f.read().split('\n')
rm  = []
filter = ['.rrsg','@2x.jp','.jxr','name','.css','example','.aws.','.jwpl','errors.stripe','addon','.mp','esu.com.ua','web.archive','google','youtube','.png','.jpeg','.jpg','wixpress','%','.webp','.gif','sentry','.avif','redbubble','xmpp.','.webm','body.content@','.js','.svg','.wiki','.py','JPG']

for x in range(len(data)):
    yn = False
    #print(x)
    for y in filter:
        #print(y)
        if y in data[x]:
            #print(yn)
            yn = True
    if yn:
        rm.append(x)
for x in reversed(range(len(rm))):
    print(data[rm[x]])
    print(len(data),x,rm[x])
    data.pop(rm[x])
datalist = {''}
for x in data:
    datalist.add(x)
    
f.close()

g = open("qbake-"+str(num)+".txt","w")
g.write('\n'.join(datalist))
g.close()

