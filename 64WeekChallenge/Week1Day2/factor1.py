def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorisation(n):
    factors = []
    for p in prime_factors(n):
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        factors.append((p, count))
    return factors

print(factorisation(int(input())))