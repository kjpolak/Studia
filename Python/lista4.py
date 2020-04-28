from math import sqrt, floor, ceil, log
import timeit

#zadanie 1
def pierwsze_imperatywna(n):
    primes = []
    for i in range(2, n):
        for j in range(2, floor(sqrt(i))+1):
            if i%j==0:
                break
        else:
            primes.append(i)
    return primes

def pierwsze_skladana(n):
    return [x for x in range(2, n) if all(x%i!=0 for i in range(2,floor(sqrt(x))+1))]

def pierwsze_funkcyjna(n):
    return list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, floor(sqrt(x))+1))),range(2, n)))

#zadanie 3
def rozklad_imperatywna(n):
    rozklad=[]
    for i in range(2,ceil(sqrt(n))):
        j=0
        while n%i==0:
            n/=i
            j+=1
        if j!=0:
            rozklad.append((i,j))
    return rozklad

def rozklad_skladana(n):
    return [(i,[j for j in range(1,int(log(n,i))) if n%(i**j) == 0][-1]) for i in pierwsze_imperatywna(n) if n%i==0]

def rozklad_funkcyjna(n):
    return list(map( lambda x: (x,list(filter(lambda i: n%(x**i)==0, range(1, int(log(n,x)))))[-1]), list(filter(lambda y: n%y==0, pierwsze_imperatywna(n)))))


def wrapper(func, *args):
     def wrapped():
         return func(*args)
     return wrapped


wrapped1 = wrapper(pierwsze_imperatywna, 20)
wrapped2 = wrapper(pierwsze_skladana, 20)
wrapped3 = wrapper(pierwsze_funkcyjna, 20)
print('Czas dla funkcji pierwsze_imperatywna: ', timeit.timeit(wrapped1, number=10))
print('Czas dla funkcji pierwsze_skladana: ', timeit.timeit(wrapped2, number=10))
print('Czas dla funkcji pierwsze_funkcyjna', timeit.timeit(wrapped3, number=10))

wrapped4 = wrapper(rozklad_imperatywna, 756)
wrapped5 = wrapper(rozklad_skladana, 756)
wrapped6 = wrapper(rozklad_funkcyjna, 756)
print('Czas dla funkcji rozklad_imperatywna: ', timeit.timeit(wrapped4, number=10))
print('Czas dla funkcji rozklad_skladana: ', timeit.timeit(wrapped5, number=10))
print('Czas dla funkcji rozklad_funkcyjna', timeit.timeit(wrapped6, number=10))
