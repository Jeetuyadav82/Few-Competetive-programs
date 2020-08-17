def findTriplets(arr, n):
    arr = sorted(arr)
    for z in range(n):
        x=arr[z]
        i=z+1;j=n-1
        while i < j:
            summ = x + arr[i] + arr[j]
            if summ == 0:
                return 1
            elif summ > 0 :
                j-=1
            else:
                i+=1
    return 0
