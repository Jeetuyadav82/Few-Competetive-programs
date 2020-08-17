def findSpecificPattern(n, arr, string):
    k=1
    l=[]
    string+='%'
    for j in range(1,len(string)):
        if string[j]==string[j-1]:
            k+=1
        else:
            l.append(k)
            k=1
    l2=[]
    for i in arr:
        k=1
        l1=[]
        i+='%'
        for j in range(1,len(i)):
            if i[j]==i[j-1]:
                k+=1
            else:
                l1.append(k)
                k=1
        if l==l1:
            l2.append(i[0:len(i)-1])
    return l2
