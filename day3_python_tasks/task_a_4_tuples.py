#4.Tuple Conversion
#Convert tuple → list → tuple after modification

def tuple_modification(my_data:tuple) -> tuple:
    
    my_list=list(my_data)
    
    my_list.append(50)
    my_list.sort()

    my_data=tuple(my_list)
    
    return my_data

my_data = (19,5,3,9,10,4)

print(my_data)
my_data = tuple_modification(my_data)
print(my_data)