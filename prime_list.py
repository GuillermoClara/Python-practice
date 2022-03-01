# This program finds all prime numbers smaller or equal than the user input


def is_prime(number):
    for num in range(2,number):
        if number % num == 0: # A prime number is divisible only by 1 and itself. Otherwise it is not prime
            return False
    
    return True
    
 
 def primes():
    limit = eval(input('Enter number: '))
    sequence = []
    for number in range(2,limit+1):
        if is_prime(number):
            sequence.append(number)
    
    
    print(sequence)
    
primes()
