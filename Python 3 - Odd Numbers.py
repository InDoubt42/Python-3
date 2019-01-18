# Testing Python 3. In progress.

def findOdd(n):
    if n % 2 == 0:
        print('This number is even.', n)
        return False
    if n % 2 != 0:
        print('This number is odd.', n)
        return True

findOdd(2)