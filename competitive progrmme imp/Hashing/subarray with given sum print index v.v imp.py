for _ in range(int(input())):
    p=0
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    i,j=0,0
    cursum=0
    while True:
        if cursum<s and j<n:
            cursum+=arr[j]
            j+=1
        elif cursum>s and i<n:
            cursum-=arr[i]
            i+=1
        elif cursum==s:
            break
        else:
            print(-1)
            p=1
            break
        
    if p==0:
        if i<j:
            print(i+1,j)
        else:
            print(-1)
        
    
    
    
    
    
    
    
    
    
    
