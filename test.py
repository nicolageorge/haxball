def cacheable(f):
  cache = {}

  def inner(n):
    if n not in cache:
      print "running for n = " + str(n)
      cache[n] = f(n)
    return cache[n]

  return inner

@cacheable
def factorial(n):
  return 1 if n <= 1 else n * factorial(n - 1)

# print factorial(5)
# print factorial(7)
