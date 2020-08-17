def subArrayExists(arr,n):
    s = set()
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum == 0 or sum in s:
            return True
        s.add(sum)
    return False


T=int(input())
while(T>0):
        
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    if(subArrayExists(arr,n)):
        print("Yes")
    else:
        print("No")
        
    T-=1


