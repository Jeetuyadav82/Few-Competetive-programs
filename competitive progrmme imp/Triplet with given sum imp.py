for i in range(int(input())):
    sz,k=map(int, input().split())
    arr=[int(i) for i in input().split()]
    arr.sort()
    res=0
    for i in range(sz):
        j=i+1
        l=sz-1
        while j<l:
            if arr[i]+arr[j]+arr[l]==k:
                res=1
                j+=1
                l-=1
                break
            
            elif arr[i]+arr[j]+arr[l]>k:
                l-=1
            else:
                j+=1
                
        if res==1:
            break
    print(res)
                
        
        