def findPlatform(arr, dep, n): 
 
    arr.sort() 
    dep.sort() 
  
    plat_needed = 1
    result = 1
    i = 1
    j = 0
 
    while (i < n and j < n): 
     
        if (arr[i] <= dep[j]): 
          
            plat_needed+= 1
            i+= 1
 
        elif (arr[i] > dep[j]): 
          
            plat_needed-= 1
            j+= 1
 
        if (plat_needed > result):  
            result = plat_needed 
          
    return result 


for i in range(int(input())):
    x=int(input())
    l1=[int(i) for i in input().split()]
    l2=[int(i) for i in input().split()]
    print(findPlatform(l1, l2, x))
    
        
    
    
        
  
    
   
            
                
    
    
    
    
        
            