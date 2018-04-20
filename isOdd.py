# determine if an integer is odd
def isOdd(n):
  return (n & 1) != 0

# use isOdd() and print out results
def Results():
  for i in range(-5,6):
    print i, isOdd(i)

Results()
