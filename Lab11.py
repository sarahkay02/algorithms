import math

# iterable object to computer powers of 2
class PowerOfTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# defines a Fibonacci iterator
class fibS:
    def __init__(self, max=1):
        self.max = max
        self.fibMinus2 = 1
        self.fibMinus1 = 1
        self.n = 1

    def __next__(self):
        if self.n <= self.max:
            self.fibOld = self.fibMinus2
            self.fibN = self.fibMinus2 + self.fibMinus1
            self.fibMinus2 = self.fibMinus1
            self.fibMinus1 = self.fibN
            self.n += 1

            return self.fibOld
        else:
            raise StopIteration

    def __iter__(self):
        return self



# compute the Fibonacci number, recursively
def fibr(n):
    if (n==1 or n==2):
        return 1
    else:
        return fibr(n-2) + fibr(n-1)


# compute the Fibonacci number, iteratively
def fibi(n):
    if (n==1 or n==2):
        return 1

    fibMinus2 = 1
    fibMinus1 = 1
    i = 3

    while (i <= n):
        fibI = fibMinus2 + fibMinus1
        fibMinus2 = fibMinus1
        fibMinus1 = fibI
        i = i + 1

    return fibI


# a generator for Fibonacci sequences
def fibg():
    fibMinus2 = 1
    fibMinus1 = 1

    while True:
        fibOld = fibMinus2
        fibI = fibMinus2 + fibMinus1
        fibMinus2 = fibMinus1
        fibMinus1 = fibI

        if fibOld > 6000000:
            raise StopIteration
        yield fibOld


# a generator that produces the first n Fibonacci numbers
def fibg2(n):
    count = 0
    fibMinus2 = 1
    fibMinus1 = 1

    while (count < n):
        fibOld = fibMinus2
        fibI = fibMinus2 + fibMinus1
        fibMinus2 = fibMinus1
        fibMinus1 = fibI
        count += 1

        if (fibOld > 6000000):
            raise StopIteration
        yield fibOld


# a generator that produces the first n prime numbers
def primes(n):
    count = 0
    num = 0

    def isPrime(num):
        # 1 is not prime, 2 is the only prime that is even
        if (num <= 2):
            if (num == 1):
                return False

            if (num == 2):
                return True

        # a prime number can't be even
        if (num % 2 == 0):
            return False

        # only need to check up to the square root of the number (so factors don't get repetitive)
        # start at 3
        for i in range(2, int(math.sqrt(num))+1):
            if (num % i == 0):
                return False
        return True


    while (count < n):
        num += 1
        if (isPrime(num) == True):
            count += 1

            # set limit on size of number computed
            if (num > 600000):
                raise StopIteration
            yield num


# a memoization version of fibr()
def fibrm(n):
    memo = {}

    def fibm(memo, n):
        if (n==1 or n==2):
            memo[n] = 1
            return 1
        else:
            if n not in memo:
                r = fibm(memo, n-2) + fibm(memo, n-1)
                memo[n] = r
                return r
            else:
                return memo[n]

    return fibm(memo, n)


# memoizes any given function
def memoize(f):
    memo = {}

    def helper(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return helper


# a recursive definition of the Factorial function
def factorial(n):
    if (n==1):
        return 1

    else:
        return n*factorial(n-1)



if __name__ == '__main__':
    for i in fibg2(10):
        print(i)


    x = 1
    for i in primes(100):
        print (x, ":", i)
        x += 1

    factorial = memoize(factorial)

    print(factorial(3))
    print(factorial(9))
    print(factorial(20))
