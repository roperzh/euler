def is_multiple_of(number, base):
  return number % base == 0

def find_sum_below(limit):
  total = 0

  for number in range(1,limit):
    if is_multiple_of(number, 3) or is_multiple_of(number, 5):
      total += number

  return total

print(find_sum_below(1000))
