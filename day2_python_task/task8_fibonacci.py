#Generating Fibonacci Series up to n terms
class FibonacciSeries:
    def __init__(self,n):
        self.n=n
        
    def generate_fibonacci(self):
        a,b=0,1
        
        for i in range(0,self.n):
            print(a)
            temp=a
            a = a+b
            b = temp
            
num=int(input("Enter an number for the fibonacci series: "))
fibanacci=FibonacciSeries(num)   
fibanacci.generate_fibonacci()      
            
            
            