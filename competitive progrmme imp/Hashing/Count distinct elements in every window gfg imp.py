def countDistinct(arr, n, k):
    for i in range(n-k+1):
        print(len(list(set(arr[i:i+k]))),end=' ')
    print()
