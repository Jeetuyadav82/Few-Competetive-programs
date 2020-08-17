for i in range(int(input())):
    a,b=map(int,input().split())
    l=[int(i) for i in input().split()]
    k,x=0,[]
    for i in l:
        p=b-i
        if p in x:
            print('Yes')
            k=1
            break
        x.append(i)
    if k==0:
        print('No')
