from math import sqrt

def tabliczka(x1,x2,y1,y2):
    print(" ", end = ' ')
    for i in range(x1, x2+1):
        print(i, end = ' ')
    for i in range(y1, y2+1):
        print("\n", i, end=' ')
        for j in range(x1,x2+1):
            print(i*j, end=' ')

#zadanie 1

def vat_faktura(lista):
    return 0.23*sum(lista)

def vat_paragon(lista):
    return sum(list(map(lambda x: x*0.23, lista)))

zakupy = [0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy) == vat_paragon(zakupy))

#zadanie 5
            
def rozklad(n):
    rozklad=[]
    for i in range(2,int(sqrt(n))):
        j=0
        while n%i==0:
            n/=i
            j+=1
        if j!=0:
            rozklad.append((i,j))
    return rozklad
    
#zadanie 4

def zaszyfruj(tekst, klucz):
    zaszyfrowany=''
    for x in tekst:
        zaszyfrowany+=chr(ord(x)^klucz)
    return zaszyfrowany

def odszyfruj(szyfr, klucz):
    return zaszyfruj(szyfr, klucz)
