def missingNumber(arr,n):
    l=[0 for i in range(100000)]
    for i in arr:
        if i>0:
            l[i-1]=1
    return l.index(0)+1