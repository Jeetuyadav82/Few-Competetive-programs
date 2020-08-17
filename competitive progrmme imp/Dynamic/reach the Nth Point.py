t=int(input())
arr=[0]*101
arr[0]=1
for j in range(1,100):
        arr[j]=arr[j-2]+arr[j-1]
for i in range(t):
    n=int(input())
    print(arr[n])