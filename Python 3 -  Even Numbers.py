# Testing Python 3. In progress.

def findEven(n):
    if n % 2 == 0:
        print(n)
        return True
    if n % 2 != 0:
        print("This number is odd.", n)
        return False
    
findEven(59)