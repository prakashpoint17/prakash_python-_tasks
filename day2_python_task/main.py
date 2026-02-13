import utils

print("Check prime number")
num=10
if utils.is_prime(num): 
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
    
print("check reversing a String")
str="hello how are you"
print(f"reverse string is : {utils.reverse_string(str)}")

print("generate fibanocci series")
value=10
print(f"the fibocacci series till {value} is : {utils.fibonacci(value)}")