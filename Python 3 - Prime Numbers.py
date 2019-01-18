# Python 3!

# Function to find prime numbers.

def findPrime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    if n <= 1:
        return False
    else:
        return True
    
findPrime(1)

