n=int(input());
for _ in range(n):
    input();
    lis1=list(map(int,input().split()));
    lis2=list(map(int,input().split()));
    dic1={}
    for i in lis1: 
        if(i in dic1):
            dic1[i]+=1;
        else:
            dic1[i]=1;
            
            
    for i in lis2: 
        if(i in dic1 and dic1[i]>=1):
            print((str(i)+" ")*dic1[i],end="");
            del dic1[i];
            
            
    if(len(dic1)>0): 
        lis=sorted(list(dic1.keys()));
        
        
    for i in lis:
        print((str(i)+" ")*dic1[i],end="");
    print();
