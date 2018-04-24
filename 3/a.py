def is_prime(number):
  for x in xrange(2, number):
    if number == x or number % x == 0:
      return False

  return True

def is_factor(number, base):
  return number % base == 0

def prime():
  x = 2
  while True:
    if is_prime(x):
      yield x

    x += 1

def prime_factors(number):
  factors = []
  prime_generator = prime()
  current_number = number

  while current_number != 1:
    next_prime = next(prime_generator)
    if is_factor(current_number, next_prime):
      current_number = current_number / next_prime
      factors.append(next_prime)
      prime_generator = prime()

  return factors

print(prime_factors(600851475143))
