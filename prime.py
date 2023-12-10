def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Encuentra números primos entre 1 y 250
primes = [num for num in range(1, 251) if is_prime(num)]

# Guarda los números primos en un archivo
with open('./results.txt', 'w') as file:
    for prime in primes:
        file.write(str(prime) + '\n')