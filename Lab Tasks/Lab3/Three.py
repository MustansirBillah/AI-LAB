x = [[0,0,0,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,0,1,1,0]]
y = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for w in range(0,5):
    for t in range(0,5):
        p = x[w][t]
        if(p==1):
            y[t][w]=p
print(y)
