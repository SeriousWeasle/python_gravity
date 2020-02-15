import math

class vec3:
    def __init__(self, comp1, comp2, comp3):
        self.c1 = comp1
        self.c2 = comp2
        self.c3 = comp3

    def length(self):
        return math.sqrt((self.c1 * self.c1) + (self.c2 * self.c2) + (self.c3 * self.c3))

    def __add__(self, other):
        comp1 = self.c1 + other.c1
        comp2 = self.c2 + other.c2
        comp3 = self.c3 + other.c3
        return vec3(comp1, comp2, comp3)

    def __sub__(self, other):
        comp1 = self.c1 - other.c1
        comp2 = self.c2 - other.c2
        comp3 = self.c3 - other.c3
        return vec3(comp1, comp2, comp3)

    def __mul__(self, other):
        if isinstance(other, vec3):
            comp1 = self.c1 * other.c1
            comp2 = self.c2 * other.c2
            comp3 = self.c3 * other.c3
        else:
            comp1 = self.c1 * other
            comp2 = self.c2 * other
            comp3 = self.c3 * other
        return vec3(comp1, comp2, comp3)

    def __truediv__(self, other):
        if isinstance(other, vec3):
            comp1 = self.c1 / other.c1
            comp2 = self.c2 / other.c2
            comp3 = self.c3 / other.c3
        else:
            comp1 = self.c1 / other
            comp2 = self.c2 / other
            comp3 = self.c3 / other
        return vec3(comp1, comp2, comp3)
    
    def x(self):
        return self.c1

    def y(self):
        return self.c2
    
    def z(self):
        return self.c3

    def comps(self):
        return [self.c1, self.c2, self.c3]