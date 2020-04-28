from itertools import permutations
from math import floor, sqrt

#zadanie 1

def pierwsze_iteracyjna(n):
    for i in range(2, n):
        for j in range(2, floor(sqrt(i))+1):
            if i%j==0:
                break
        else:
            yield i


print([x for x in pierwsze_iteracyjna(20)])

#zadanie 2

def eval(word, dict):
    i = 1
    number = 0
    for letter in word[::-1]:
        number+=dict[letter]*i
        i*=10
    return number

def kryptarytm(x1, x2, x3):
    chars = set(''.join(x1+x2+x3))
    if len(chars)>10:
        return False
    all_possibility = [dict(zip(chars, x)) for x in permutations([0,1,2,3,4,5,6,7,8,9],len(chars))]
    for possibility in all_possibility:
        if possibility[x1[0]]*possibility[x2[0]]*possibility[x3[0]]==0:
            continue
        if eval(x1, possibility)+eval(x2, possibility)==eval(x3, possibility):
            return possibility


