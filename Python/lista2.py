import itertools

class Formula():
    def __init__(self, formula):
        self.formula = formula
    
    def __str__(self):
        return self.formula
    
    def oblicz(self, vars):
        return self.formula.oblicz(vars)

    def tautologia(self, vars):
        all_possibility =[dict(zip(vars,x)) for x in itertools.product([True, False],repeat=len(vars))]
        if all([self.formula.oblicz(x) for x in all_possibility]):
            return True
        return False

class Not(Formula):
    def __init__(self, right):
        self.right = right

    def __str__(self):
        return "~(%s)" % self.right

    def oblicz(self, vars):
        return not self.right.oblicz(vars)
    
class And(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s ∧ %s)" % (self.left, self.right)

    def oblicz(self, vars):
        return self.left.oblicz(vars) and self.right.oblicz(vars)
    
class Or(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s ∨ %s)" % (self.left, self.right)

    def oblicz(self, vars):
        return self.left.oblicz(vars) or self.right.oblicz(vars)
    
class Impl(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s ⇒ %s)" % (self.left, self.right)

    def oblicz(self, vars):
        return (not self.left.oblicz(vars)) or self.right.oblicz(vars)
    
class Equiv(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(%s ⇔ %s)" % (self.left, self.right)

    def oblicz(self, vars):
        return self.left.oblicz(vars)==self.right.oblicz(vars) 
    
class T(Formula):
    def __init__(self):
        pass
    
    def __str__(self):
        return "true" 

    def oblicz(self, vars):
        return True
    
class F(Formula):
    def _init__(self):
        pass
    
    def __str__(self):
        return "false"

    def oblicz(self, vars):
        return False
    
class Zmienna(Formula):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def oblicz(self, vars):
        return vars[self.name]

p1 = Formula(Impl(Zmienna('x'), And(Zmienna('y'), T())))
print(p1.__str__())
vars = dict(zip(['x', 'y'], [False, True]))
print(p1.oblicz(vars))
print(p1.tautologia(['x', 'y']))

p2 = Formula(Or(Zmienna('p'), Not(Zmienna('p'))))    
print(p2.__str__())
vars2=dict(zip(['p'], [True]))
print(p2.oblicz(vars2))
print(p2.tautologia(['p']))

