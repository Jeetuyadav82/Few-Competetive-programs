# Python3

def get_ans(m, n, arr):
    count = 0
    left = m*n
    while(left>0):
        
        # Going left to right
        i = count
        for j in range(count, n-count):
            print(arr[i][j], end = ' ')
            left -= 1
        
        # Going top to bottom
        j = n-1-count
        for i in range(1+count, m-count):
            print(arr[i][j], end = ' ')
            left -= 1
        
        if not left: break
        
        # Going right to left
        i = m-1-count
        for j in reversed(range(count, n-1-count)):
            print(arr[i][j], end = ' ')
            left -= 1
        
        # Going bottom to top
        j = count
        for i in reversed(range(count+1, m-1-count)):
            print(arr[i][j], end = ' ')
            left -= 1
            
        count += 1
    
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        m, n = list(map(int, input().split()))
        tmp = list(map(int, input().split()))
        arr = []
        for i in range(m):
            arr.append(tmp[n*i:n*(i+1)])
        # print(arr)
        get_ans(m, n, arr)
        print()
