from collections import defaultdict 
  
def findSubarraySum(arr, n, Sum):  
   
   
    prevSum = defaultdict(lambda : 0) 
    
    res = 0 
    
    currsum = 0 
    
    for i in range(0, n):   
    
       
        currsum += arr[i]

    
       
        if currsum == Sum:   
            res += 1         
    
        
        if (currsum - Sum) in prevSum: 
            res += prevSum[currsum - Sum]

          

        prevSum[currsum] += 1

       
    return res  
   
for i in range(int(input())):
    k=int(input())
    l=[int(i) for i in input().split()]
    gs=int(input())
    t=findSubarraySum(l, k, gs)
    print(t)
