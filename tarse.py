f = open("testing.txt","r",encoding='utf-8')
data = f.read().split('\n')
f.close()

bsize = 4000
for x in range(int(len(data)/bsize)+1):
    g = open("city-"+str(x)+".txt","a",encoding='utf-8')
    g.write('\n'.join(data[x*bsize:(x+1)*bsize]))
    g.close()
