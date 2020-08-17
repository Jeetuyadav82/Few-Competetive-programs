for i in range(int(input())):
    k=int(input())
    l=[int(j) for j in input().split()]
    cursum=l[0]
    maxsum=l[0]
    for i in range(1,k):
        cursum=max(l[i],l[i]+cursum)
        if cursum>maxsum:
            maxsum=cursum
    print(maxsum)
