def transforms(m_str, c_str):
    nm = len(m_str)
    nc = len(c_str)
    
    dp = [[0 for i in range(nc)] for j in range(nm)]
    
    for i in range(nm):
        for j in range(nc):
            dp[i][j] = dp[i-1][j]
            if m_str[i] == c_str[j]:
                if j == 0:
                    dp[i][j] += 1
                else:
                    dp[i][j] += dp[i-1][j-1]
                    
    print(dp)
    return dp[nm-1][nc-1]


for _ in range(int(input())):
    m_str = input()
    c_str = input()
    print(transforms(m_str, c_str))
