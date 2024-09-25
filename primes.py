"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2  # Starting number to check for primes
    
    if number_of_primes < 1:
        raise ValueError

    while len(list) < number_of_primes:
        # Check if num is prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            list.append(num)
        num += 1
    
    return list
