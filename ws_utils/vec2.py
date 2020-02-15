import math

class vec2:
    def __init__(self, comp1:float, comp2:float):
        self.c1 = comp1
        self.c2 = comp2
    
    def length(self):
        return math.sqrt((self.c1 * self.c1) + (self.c2 * self.c2))
    
    def __add__(self, other):
        comp1 = self.c1 + other.c1
        comp2 = self.c2 + other.c2
        return vec2(comp1, comp2)

    def __sub__(self, other):
        comp1 = self.c1 - other.c1
        comp2 = self.c2 - other.c2
        return vec2(comp1, comp2)

    def __mul__(self, other):
        if isinstance(other, vec2):
            comp1 = self.c1 * other.c1
            comp2 = self.c2 * other.c2
        else:
            comp1 = self.c1 * other
            comp2 = self.c2 * other
        return vec2(comp1, comp2)

    def __rmul__(self, other):
        if isinstance(other, vec2):
            comp1 = self.c1 * other.c1
            comp2 = self.c2 * other.c2
        else:
            comp1 = self.c1 * other
            comp2 = self.c2 * other
        return vec2(comp1, comp2)

    def __truediv__(self, other):
        if isinstance(other, vec2):
            comp1 = self.c1 / other.c1
            comp2 = self.c2 / other.c2
        else:
            comp1 = self.c1 / other
            comp2 = self.c2 / other
        return vec2(comp1, comp2)

    def x(self):
        return self.c1

    def y(self):
        return self.c2

    def comps(self):
        return [self.c1, self.c2]