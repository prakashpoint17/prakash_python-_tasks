# Function to check if a number is prime
def prime_check(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input from the user
num = int(input("Enter the number to check for prime: "))

# Check if the number is prime
if prime_check(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")