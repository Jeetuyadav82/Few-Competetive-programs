l=[0]*(100000+1)
l[0]=0
l[1]=1
l[2]=2
for j in range(3,100000+1):
    l[j]=max(j,l[j//2]+l[j//3]+l[j//4])
    
for i in range(int(input())):
    k=int(input())
    print(l[k])
