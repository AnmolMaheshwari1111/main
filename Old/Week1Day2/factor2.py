def prime_factors(number: int) -> list:
    """
    Returns a list of prime factors of a given number.
    """
    factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return sorted(factors)

def factorisation(number: int) -> list:
    """
    Returns a list of tuples containing prime factors and their counts.
    """
    factor_counts = []
    for p in prime_factors(number):
        count = 0
        while number % p == 0:
            number //= p
            count += 1
        factor_counts.append((p, count))
    return factor_counts

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        result = factorisation(n)
        print(f"Factorisation of {n}: {result}")
    except ValueError:
        print("Error: Please enter an integer value.")