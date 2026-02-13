#Python program to accept user name and greet them with their name
class Greet:
    def __init__ (self,name):
        self.name=name
        
    def greet_user(self):
        print(f"Hello {self.name}, welcome to the world of python programming!")

#Accepting user name
name=input("Please enter your pretty name: ")
greeting=Greet(name)
greeting.greet_user()