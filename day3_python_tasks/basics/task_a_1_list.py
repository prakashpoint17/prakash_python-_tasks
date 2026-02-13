#List Manipulation
#Add, remove, sort, reverse items
#Remove duplicates without using set()

class List_operations:
    def __init__(self,data_lst:list):
        self.data_lst=data_lst
        
    def add_item(self,value:float):
        self.data_lst.append(value)
        return self.data_lst
    
    def remove_item(self,value:float):
        self.data_lst.remove(value)
        return self.data_lst
    
    def sort_items(self):
        self.data_lst.sort()
        return self.data_lst
    
    def reverse_items(self):
        self.data_lst.reverse()
        return self.data_lst
    
    def remove_duplicate_items(self):
        temp_dict={}
        unique_list=[]
        
        for num in self.data_lst:
            if num not in temp_dict:
                temp_dict[num]= True
                unique_list.append(num)
        
        self.data_lst = unique_list
        return self.data_lst
    
list1=[12,32,57,20,12,32,67,20]
operation = List_operations(list1)
print(operation.add_item(10))
print(operation.remove_item(12))
print(operation.sort_items())
print(operation.reverse_items())
print(operation.remove_duplicate_items())
