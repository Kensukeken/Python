from functools import reduce

def alpha(x, p):

    result = 0
    power = p
    while power <= x:
        result += int(x // power)
        power *= p
    return result

def product_of_primes(x):
  
    primes = []
    prime_factors = []
    for i in range(2, x+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    
    for p in primes:
        prime_factors.append(p ** alpha(x, p))
    
    return reduce(lambda x, y: x*y, prime_factors)
