for i in range(int(input())):
    a=input()
    k=int(input())
    l=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            p=a[i:j]
            if len(list(set(p)))==k:
                l.append(len(p))
    if len(l)>0:
        print(max(l))
    else:
        print(-1)
