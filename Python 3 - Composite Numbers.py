# Testing Python 3. In progress.

def findComposite(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return False
    if n % 2 == 0:
        return True
    if n % 3 == 0:
        return True
    if n % 5 == 0:
        return True
    if n % 7 == 0:
        return True
    else:
        return False
    
findComposite(19)