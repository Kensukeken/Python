import math

def prime_count(n):

    if n < 2:

        return 0

    # Calculate the values of the constant terms

    x = int(math.sqrt(n))

    pi_x = prime_count(x)

    pi_x2 = prime_count(int(math.sqrt(x)))

    # Initialize the arrays

    a = [0] * (x + 1)

    b = [0] * (x + 1)

    for i in range(1, x + 1):

        a[i] = i - 1

        b[i] = n // i - 1

    for p in range(2, pi_x2 + 1):

        if a[p] == a[p - 1]:

            continue

        sp = a[p - 1]

        for q in range(1, x + 1):

            if p * p > b[q]:

                break

            b[q] -= b[q * p] - sp

        for q in range(x, p * p - 1, -1):

            a[q] -= a[q // p] - sp

    return b[1] + pi_x - 1

# Example usage

n = 100

count = prime_count(n)

print(f"The number of primes less than or equal to {n} is {count}.")
