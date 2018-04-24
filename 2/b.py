class Fibonacci(object):
  def __init__(self):
    self.prev1 = 0
    self.prev2 = 1

  def next(self):
    result = self.prev1 + self.prev2
    self.prev1 = self.prev2
    self.prev2 = result
    return result

def is_even(number):
  return number % 2 == 0

def resolve():
  fibo = Fibonacci()
  result = 0
  nextFibo = fibo.next()

  while nextFibo <= 4000000:
    if is_even(nextFibo):
      result += nextFibo
    nextFibo = fibo.next()

  return result

print(resolve())
