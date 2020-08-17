for i in range(int(input())):
    k=int(input())
    l=[int(i) for i in input().split()]
    p=set(l)
    max_ele=max(l)
    res=0
    for i in range(k):
        for j in range(i+1,k):
    
            if l[i]+l[j]>max_ele:
                continue
            elif l[i]+l[j] in p:
                res+=1
    if res==0:
        res=-1
    print(res)
                