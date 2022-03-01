# The Goldbach conjecture asserts that every even integer greater than 2 can be expressed as the sum of two primes.

def is_prime(number):
    for num in range(2,number):
        if number % num == 0: # A prime number is divisible only by 1 and itself. Otherwise it is not prime
            return False
    
    return True
    
 
def primes(limit):
    sequence = []
    for number in range(1,limit):
        if is_prime(number):
            sequence.append(number)
    return sequence
    
def goldbach():
    user_num = eval(input('Enter number: '))

    if user_num % 2 == 0:
        prime_seq = primes(user_num)
        for i in reversed(prime_seq):
            for k in prime_seq:
                if (i+k) == user_num:
                    print(k,'+',i)
                    return
    else:
        print('number wasnt even')

goldbach()
