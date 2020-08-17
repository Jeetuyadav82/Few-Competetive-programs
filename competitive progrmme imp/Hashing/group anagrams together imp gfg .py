for i in range(int(input())):
    k=int(input())
    l=[i for i in input().split()]
    p=[]
    l1=[]
    for i in l:
        x=0
        if i not in l1:
            for j in l:
                if sorted(i)==sorted(j):
                    x+=1
                    l1.append(j)
            p.append(x)
    print(*sorted(p))
