for i in range(int(input())):
    k=int(input())
    a=input()
    p=0
    q={}
    for i in a:
        if i in q:
            q[i]=2
        else:
            q[i]=1
    for i in a:
        if q[i]==1:
            print(i)
            p=1
            break
    if p==0:
        print(-1)
