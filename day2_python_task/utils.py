#utilities package [utils.py]
    
#To check prime number(input : n , output : True/False)
def is_prime(n:int) -> bool:
   
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if i%n != 0:
            return True
        else:
            return False
        
#To Reverse an input string (input: s:str , Output: reversed string : str)
def reverse_string(s:str) -> str:
   
    try:
        if s != str(s):
            raise ValueError("Please Enter a String.")
        else:
            revstr = s[::-1]
            return str(revstr)
        
    except ValueError as e:
        print(e)
        
#To Generate fibonacci series (input : num : int, Output : fibonacci series [list])
def fibonacci(n:int) -> list:
    
    try:        
        a,b = 0,1
        fseries=[]
        
        for i in range(a,n):
            fseries.append(a)
            temp=a
            a=a+b
            b=temp
            
        return fseries
            
    except Exception as e:
        print(e)