#Check even or odd number
def even_or_odd(num:int):

    if number % 2 == 0:
        print(f"{number} is a even number")  
    else:
        print(f"{number} is an odd number")
    
number = int(input("Enter a Number:"))
even_or_odd(number)