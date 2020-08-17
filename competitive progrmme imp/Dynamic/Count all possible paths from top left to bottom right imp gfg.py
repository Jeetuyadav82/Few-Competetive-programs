for i in range(int(input())):
    a,b=map(int,input().split())
    
    l=[[0]*b for i in range(a)]
    
    for i in range(b):
        l[0][i]=1
        
    for j in range(a):
        l[j][0]=1
        
    for i in range(1,a):
        for j in range(1,b):
            l[i][j]=l[i-1][j]+l[i][j-1]
            
    print(l[a-1][b-1]%(1000000007))
