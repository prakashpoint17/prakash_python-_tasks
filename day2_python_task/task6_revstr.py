def rev_string(s:str) -> str:
    try:
        if type(s) != str:
            raise ValueError("enter a string")
        return s[::-1]
    
    except ValueError as e:
        print(e)

str1=input("Enter the string to be reversed : ")

print(f"reversed string : {rev_string(str1)}")