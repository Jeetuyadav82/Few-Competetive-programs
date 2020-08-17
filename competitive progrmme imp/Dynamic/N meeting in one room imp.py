# Sort array by their finish time and compare if next meeting's start time is greater than prev's end time then print its index;

for i in range(int(input())):
    x=int(input())
    l1=[int(i) for i in input().split()]
    l2=[int(i) for i in input().split()]
    arr=[]
    
    for j in range(x):
        arr.append([l2[j],l1[j]])
        
    arr.sort()
   
    y=arr[0][1]
    c=0
    z=[]
    for i in arr:
        if i[1]>=y:
            c+=1
            y=i[0]
            z.append([i[1],i[0]])
    
    for i in z:
        for j in range(x):
            if l1[j]==i[0] and l2[j]==i[1]:
                print(j+1,end=" ")
    print()
    
        
            