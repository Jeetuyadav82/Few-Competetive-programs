# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text,l):
    opening_brackets_stack = []
    
    for next in text:
        
        if next in "([{":

            opening_brackets_stack.append(next)

            l[0]+=1
            pass

        elif next in ")]}":
            if len(opening_brackets_stack)==0:
                l[0]+=1
                opening_brackets_stack.append(next)
                return opening_brackets_stack
            l[0]+=1
            if opening_brackets_stack[-1] =="(" and next == ")":
                opening_brackets_stack.pop()

            elif opening_brackets_stack[-1] =="{" and next == "}":
                opening_brackets_stack.pop()

            elif opening_brackets_stack[-1] =="[" and next == "]":
                opening_brackets_stack.pop()
                
            else:
                return opening_brackets_stack
            pass
        else:
            l[0]+=1
        
    return opening_brackets_stack
                


def main():
    text = input()
    l=[0]
    mismatch = find_mismatch(text,l)

    if mismatch ==[]:
        print("Success")
    else:
        print("Not success")
        
    


if __name__ == "__main__":
    main()
