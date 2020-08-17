def fun(n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            count +=1
    return count        
for _ in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    l = {}
    sum = 0
    result = 0
    for i in d:
        sum += i
        x = l.get(sum,0)
        l[sum] = x+1 
    for key in l:
        if key ==0:
            result += l[0]
            result += fun(l[0]) 
        else:
            result += fun(l[key])
    print(result)
