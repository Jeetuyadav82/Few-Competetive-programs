for i in range(int(input())):
    a=input()

    p='$'
    for i in range(len(a)):
        if p[-1]=='0' and a[i]=='0':
            q=1
        else:
            p+=a[i]
    x=0   
    for i in range(len(p)-2):
        if p[i:i+3]=='101':
            x+=1
    print(x)
            
