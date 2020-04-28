import random

#zadanie 1
wynik_wyborow={}
lines = [line.rstrip('\n') for line in open('wybory.txt', encoding='utf8')]
lines = list(filter(lambda a: a != '', lines))
lines[0]='PSL'
#print(lines)
i=0
while i<len(lines):
    if not lines[i][0].isnumeric():
        dict={}
        j=i+1
        while lines[j][0].isnumeric():
            dict[lines[j]]=int(lines[j+1])
            j+=2
            if j>=len(lines):
                break
    wynik_wyborow[lines[i]]=dict
    i=j        
        


def wybory(wynik_wyborow, liczba_miejsc):
    suma = sum([sum(value.values()) for value in wynik_wyborow.values()])
    ponadprog = {}
    wyniki_partii =[]
    for key in wynik_wyborow:
        suma_partii = sum(wynik_wyborow[key].values())
        if suma_partii/suma >= 0.05:
            ponadprog[key] = wynik_wyborow[key]
            wyniki_partii+=[(suma_partii/i, key) for i in range(1, liczba_miejsc+1)]
    wyniki_partii = [i[1] for i in sorted(wyniki_partii, reverse=True)[:liczba_miejsc]]
    wybrani = []
    for key in ponadprog:
        liczba_mandatow = wyniki_partii.count(key)
        wybrani+=sorted(ponadprog[key], key=ponadprog[key].get, reverse=True)[:liczba_mandatow]
    return wybrani

print(wybory(wynik_wyborow, 12))

#zadanie 2

def pierwiastek(n):
    sum = 0
    for i in range(1, n, 2):
        sum +=i
        if (sum <= n)and(sum+2+i>n):
            return (i+1)/2

print(pierwiastek(16))
        
#zadanie 4

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    tekst = [w for w in tekst.split() if len(w)<dl_slowa+1]
    if len(tekst)>liczba_slow:
        id_remove = random.sample(range(0, len(tekst)), len(tekst)-liczba_slow)
        for i in sorted(id_remove, reverse =True):
            del tekst[i]
    return ' '.join(tekst)

tekst = "Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej."


print(uprosc_zdanie(tekst, 10, 5))
