def pairs(l, k):
    s = {}
    count = 0
    for i in l:
        s[i] = i
    for j in l:
        g = j+k
        if g in s:
            count +=1
    return count

    
a,k=map(int,input().split())
l=[int(i) for i in input().split()]
x=pairs(l,k)
print(x)
