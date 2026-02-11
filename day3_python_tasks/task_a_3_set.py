#3.Set Operations
#Find common items between two lists using sets

def find_common_item(list1:list,list2:list) -> list:
    
    set1=set(list1)
    set2=set(list2)
    common_items = list(set1.intersection(set2))
    
    return common_items
    
list1=[1,7,4,5,3,9]
list2=[3,9,0,8,2,4]

result=find_common_item(list1,list2)
print(result)