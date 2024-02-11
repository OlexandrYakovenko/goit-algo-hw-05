
def caching_fibonacci():
    ''' Function calculates Fibonacci-numbers with using cashing '''

    cache = dict()

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n] #using cache

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) #calculating number for cache
        return cache[n] #return number from cache

    return fibonacci #return function

func=caching_fibonacci() #saving function for calculating number Fibonacci
print(func(10)) #calculates all numbers in cache from 2 to 10, numbers <2 is not in cache
print(func(5)) #number for 5 already is in cache
print(func(7)) #number for 7 already is in cache
