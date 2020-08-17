for _ in range(int(input())) :
    n = int(input())
    arr = list(map(int,input().strip().split()))
    b=[0]*(n+1)
    for i in arr:
        b[i]+=1
    for i in range(1,n+1):
        print(b[i],end=" ")
    print()
