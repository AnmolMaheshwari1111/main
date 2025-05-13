import timeit

def prime_factors_1(n):
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

def prime_factors_2(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def factorisation_1(n):
    factors = []
    for p in prime_factors_1(n):
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        factors.append((p, count))
    return factors

def factorisation_2(n):
    factor_counts = []
    for p in prime_factors_2(n):
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        factor_counts.append((p, count))
    return factor_counts

def test_performance():
    n = int(input("Enter a number: "))
    t1 = timeit.timeit(lambda: factorisation_1(n), number=1000)
    t2 = timeit.timeit(lambda: factorisation_2(n), number=1000)
    print(f"Factorisation 1: {t1} seconds")
    print(f"Factorisation 2: {t2} seconds")
    if t1 < t2:
        print("Factorisation 1 is faster.")
    elif t1 > t2:
        print("Factorisation 2 is faster.")
    else:
        print("Both programmes have the same performance.")

if __name__ == "__main__":
    test_performance()