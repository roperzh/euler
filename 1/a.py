"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def is_multiple_of(number, base):
  return number % base == 0

def find_sum_below(limit):
  total = 0

  for number in xrange(1,limit):
    if is_multiple_of(number, 3) or is_multiple_of(number, 5):
      total += number

  return total

print(find_sum_below(1000))
