for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[0]*30
    if n==1:
        print(0)
    elif n==2:
        print(min(arr))
    else:
        dp[0]=arr[0]
        dp[1]=arr[1]        
        for i in range(2,n):
            dp[i]=arr[i]+min(dp[i-1],dp[i-2])
        print(min(dp[n-1],dp[n-2]))