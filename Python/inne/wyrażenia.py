class DzieleniePrzezZero(Exception):
    pass

class BrakZmiennej(Exception):
    pass

class Wyrazenie():
    def __str__(self):
        pass
    
    def oblicz(self, vars):
        pass


class Dodaj(Wyrazenie):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s + %s)" % (self.left, self.right)

    def oblicz(self, vars):
        return self.left.oblicz(vars)+self.right.oblicz(vars)

    
class Odejmij(Wyrazenie):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s - %s)" % (self.left, self.right)

    def oblicz(self, vars):
        return self.left.oblicz(vars)-self.right.oblicz(vars)

class Razy(Wyrazenie):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s * %s)" % (self.left, self.right)

    def oblicz(self, vars):
        return self.left.oblicz(vars)*self.right.oblicz(vars)

class Dziel(Wyrazenie):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s / %s)" % (self.left, self.right)

    def oblicz(self, vars):
        right = self.right.oblicz(vars)
        if right == 0:
            raise DzieleniePrzezZero('Próbowano dzielić przez zero w wyrażeniu: '+ self.right.__str__())
        else:
            return self.left.oblicz(vars)/right
        '''
        try:
            right = self.right.oblicz(vars)
            if right == 0:
                raise DzieleniePrzezZero
            else:
                return self.left.oblicz(vars)/right
        except DzieleniePrzezZero:
            print('Próbowano dzielić przez zero w wyrażeniu: '+ self.right.__str__())
            '''
        '''
        try:
            return self.left.oblicz(vars)/self.right.oblicz(vars)
        except ZeroDivisionError:
            print('Dzielenie przez zero nie jest dozwolone')
        '''

class Stala(Wyrazenie):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def oblicz(self, _):
        return self.value

class Zmienna(Wyrazenie):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def oblicz(self, vars):
        if self.name not in vars:
            raise BrakZmiennej('Brak zmiennej w pamięci')
        else:
            return vars[self.name]
        '''
        try:
            if self.name not in vars:
                raise BrakZmiennej('Brak zmiennej w pamięci')
            else:
                return vars[self.name] 
        except BrakZmiennej:
            print('Brak zmiennej w pamięci')
        '''
        '''
        try:
            return vars[self.name]
        except KeyError:
            print('Brak zmiennej w pamięci')

        '''
vars = dict(zip(['x', 'y', 'z'], [1,5,3]))
wyrazenie = Stala('6')
wyrazenie2 = Razy(Dodaj(Zmienna("x"), Stala(2)), Zmienna("y"))
wyrazenie3 = Dziel(Stala(7), Stala(0))
print(wyrazenie3.oblicz(vars))
#print(wyrazenie2.__str__())
