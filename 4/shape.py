import math

class Shape:
    def __init__(self,input):
        self.polysides = {
            'triangle':3,
            'square':4,
            'pentagon':5,
        }
        self.type = input[0]
        self.measurement = float(input[1])
        self._get_perimeter()
        self._get_area()

    def _get_perimeter(self):
        if self.type != 'circle':
            self.perimeter = self.measurement*self.polysides[self.type]
        else:
            self.perimeter = 2*math.pi*self.measurement

    def _get_area(self):
        if self.type == 'circle':
            self.area = math.pi*self.measurement**2
        elif self.type == 'triangle':
            self.area = (math.sqrt(3)/4)*self.measurement**2
        elif self.type == 'square':
            self.area = self.measurement**2
        elif self.type == 'pentagon':
            self.area = .25*(math.sqrt(5*(5+2*math.sqrt(5)))*self.measurement**2)

    @property
    def output(self):
        if self.type != 'circle':
            m = 'side length'
        else:
            m = 'radius'
        return f'A {self.type} with {m} {self.measurement} u has a perimeter of {round(self.perimeter,2)} u and an area of {round(self.area,2)} u^2'