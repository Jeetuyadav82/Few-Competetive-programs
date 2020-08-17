from itertools import combinations
for i in range(int(input())):
    a,b=map(int,input().split())
    l=[int(i) for i in input().split()]
    p=combinations(l,4)
    y=0
    l1,l2=[],[]
    for i in p:
        if sum(i)==b:
            x=list(i)
            x.sort()
            if x not in l1:
                l2.append(x)
                y=1
            l1.append(x)
    l2.sort()
    for j in l2:
        print(*j,end=' $')
    if y==0:
        print(-1)
    else:
        print()
    
