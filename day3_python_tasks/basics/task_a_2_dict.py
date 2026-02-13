#2.Dictionary Operations
#Count occurrences of each character in a string

def char_occurrences(s:str)-> dict:
    
    my_dict={}
    
    for i in s:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
            
    return my_dict

s="interpreter"
result = char_occurrences(s)
for i in result:
    print(f"{i} occurs {result[i]} time.")