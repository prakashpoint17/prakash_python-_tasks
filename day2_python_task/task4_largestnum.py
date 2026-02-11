class GreatestNumber:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3

    def using_elif(self):
        
        if num1 >= num2 and num1 >= num3:
            largest = num1
        elif num2 >= num1 and num2 >= num3:
            largest = num2
        else:
            largest = num3
    
        return largest
        
    def using_maxfunc(self):
        largest = max(num1, num2, num3)
        return largest
    
    def using_singlelineif(self):
        largest = num1 if (num1 >= num2 and num1 >= num3) else (num2 if num2 >= num3 else num3)
        return largest
        
#using elif 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

greatest = GreatestNumber(num1,num2,num3)
print(f"The largest number among {num1}, {num2}, and {num3} is: {greatest.using_elif()}")

