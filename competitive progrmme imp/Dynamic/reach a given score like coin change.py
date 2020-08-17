for i in range(int(input())):
    k=int(input())
    dp=[0]*(k+1)
    dp[0]=1
    
    for i in range(3,k+1):
        dp[i]+=dp[i-3]
        
    for j in range(5,k+1):
        dp[j]+=dp[j-5]
        
    for j in range(10,k+1):
        dp[j]+=dp[j-10]
        
    print(dp[k])
