def isPrime(number):
    for i in range(1, number, -1):
        if number % i == 0:
            return False
    return True

def factorPrime(number):
    for i in range(1, number, -1):
            if isPrime(i):
                if number % i == 0:
                    return i

print(factorPrime(600851475143))
