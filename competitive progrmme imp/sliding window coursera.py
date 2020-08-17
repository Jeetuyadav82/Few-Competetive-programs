from collections import deque
def printMax(arr, n, k): 
      
    Qi = deque() 
   
    for i in range(k): 
        
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 
       
        Qi.append(i); 
          

    for i in range(k, n): 
          

        print(str(arr[Qi[0]]) + " ", end = "") 
        while Qi and Qi[0] <= i-k: 
              
            # remove from front of deque 
            Qi.popleft()  
          
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 
    
        Qi.append(i) 
      
    print(str(arr[Qi[0]])) 

k=int(input())
l=[int(i) for i in input().split()]
m=int(input())

printMax(l, k, m)

