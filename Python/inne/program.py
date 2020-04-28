class Program():
    def __srt__(self):
        pass

    def wykonaj(self, vars):
        pass

class Przypisz(Program):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        #dopisz do pamiętanych
    def __str__(self):
        return "%s = %s" %(self.name, self.value)

    def wykonaj(self, vars):
        TODO

class Warunek(Program):
    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        return 'if'+self.conditon

    def wykonaj(self, vars):
        TODO

        
class Petla(Program):
    def __init__(self, name, start, stop):
        self.name = name
        self.start = start
        self.stop = stop
        #dopisz do pamiętanych
    def __srt__(self):
        return 'for %s = %s to %s' % (self.name, self.start, self.stop)

    def wykonaj(self, vars):
        TODO

program1=[[Przypisz('z', 5)], [Warunek('z')]]
print(program1.__str__())

