import sys
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

        if res>0:
            return res

       
    return res  

def solution(A):
  p=sum(A)
  x=p//2
  
  while(1):
      
    y=findSubarraySum(A,len(A),x )
    if y>0 or x<0:
      break
    x-=1
  return p-(2*x)
    
    
  
  pass


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
