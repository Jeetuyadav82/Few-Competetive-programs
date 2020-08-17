for i in range(int(input())):
    k=int(input())
    l=input().split(' ')
    p={}
    for j in l:
        p[j]=''
    for i in range(1,k+1):
        if str(i) not in p:
            print(i)
            break
