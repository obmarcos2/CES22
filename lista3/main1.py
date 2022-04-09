from math import sin
pi = 3.1416

class Triangle():
    var = 1
    def __init__(self, l1, l2, angle):
        self.l1 = l1
        self.l2 = l2
        self.angle = angle

    def __repr__(self):
        return (f'Triangle({self.l1!r}, ' f'{self.l2!r}, ' f'{self.angle!r})' )
    #metodo de instancia. Necessita de instancia criada para utilizacao
    #e de eventuais variaveis dela. Relevante caso queiramos mudar
    #parametros de instancia dada
    def area(self):
        return self.paralelogramo_area(self.l1, self.l2, self.angle)/2
    #metodo estatico. Nao usa instancia ou classe, apenas retorna valor
    #de interesse desejado, sem a necessidade de ter haver a instancia
    @staticmethod
    def paralelogramo_area(a, b, angle):
        return a*b*sin(angle*pi/180)
    #metodo de classe. Acessam apenas a classe, podendo acessar o que
    #nao diz respeito a uma instancia
    @classmethod
    def equilatero_unitario(cls):
        cls.var = 2
        return cls(1, 1, 60)

t = Triangle(10, 10, 45)
print(t)
v = t.area
print(v)
print(Triangle.paralelogramo_area(5, 5, 90))
u = Triangle.equilatero_unitario()
print(u)
