for i in range(int(input())):
    string = input()
    first = {0: 0}  
    balance = 0     
    best = ""       
    for i, c in enumerate(string):             
        balance += 1 if c == "1" else -1       
        if balance not in first:               
            first[balance] = i+1               
        elif i - first[balance] > len(best):
            best = string[first[balance]:i+1]  
    print(len(best))  
                
