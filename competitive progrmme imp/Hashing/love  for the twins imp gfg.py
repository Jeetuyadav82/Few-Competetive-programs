t=int(input())

for j in range(t):
    n=int(input())
    l=list(input().split())
    ll=set(l)
    c=0
    for i in ll:
        c+=((l.count(i)//2)*2)
    print(c)
