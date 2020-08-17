for _ in range(int(input())):
    l=[]
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(0,len(a)-1,2):
        l+=[[a[i],a[i+1]]]
    l=sorted(l,key=lambda l:l[0])
    #print(l)
    #print(len(l))
    q=1
    while q < len(l):
    #print(q)
        if l[q][0]<=l[q-1][1]:
    
            l.insert(q + 1, ([l[q - 1][0], max( l[q][1],l[q-1][1])]))
            #print(l)
            l.pop(q)
            #print(q)
            l.pop(q-1)
            #print(l)
            
        else:
            #print(q)
            q+=1
    for i in range (len(l)):
        print (l[i][0],end=" ")
        print (l[i][1],end=" ")
    print()
