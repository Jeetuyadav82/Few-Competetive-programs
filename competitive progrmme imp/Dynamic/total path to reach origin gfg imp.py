for i in range(int(input())):
    a,b=map(int,input().split())
    l=[[0]*(b+1) for i in range(a+1)]
    for i in range(a+1):
        l[i][0]=1
    for j in range(b+1):
        l[0][j]=1
    
    for i in range(1,a+1):
        for j in range(1,b+1):
            l[i][j]=l[i-1][j]+l[i][j-1]
    print(l[a][b])


'''
def Total_Path(a,b):
    if a==0 or b==0:
        return 1
    return Total_Path(a-1,b)+Total_Path(a,b-1)
    
    
for i in range(int(input())):
    a,b=map(int,input().split())
    p=Total_Path(a,b)
    print(p)
    '''
