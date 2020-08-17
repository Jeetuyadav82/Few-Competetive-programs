a=input()
b=input()
l2= [[0]*(len(b) + 1) for i in range(len(a) + 1)]
for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i==0 or j==0:
            l2[i][j]=0
        elif a[i-1]==b[j-1]:
            l2[i][j] = l2[i-1][j-1]+1
        else:
            l2[i][j]=max(l2[i-1][j],l2[i][j-1])
x=max(*l2)
print(max(x))