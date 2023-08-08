from math import sqrt
class Punto():
    
    def __init__(self, punto_x, punto_y):
        self.punto_x = punto_x
        self.punto_y = punto_y

    def imprimir_coordenadas(self):
        print("El punto esta en las coordenadas, x:",self.punto_x, ", y:",self.punto_y)

    def mover(self):
        pivot = self.punto_y
        self.punto_y = self.punto_x
        self.punto_x = pivot
        print("El punto esta en las coordenadas, x:",self.punto_x, ", y:",self.punto_y)

    def calcular_distancia(self):
        x_2 = int(input("Ingrese la coordenada en x:"))
        y_2 = int(input("Ingrese la coordenada en y:"))

        print("La distancia es de:", sqrt((self.punto_x - x_2)**2 + (self.punto_y - y_2)**2))

c = Punto(3,1)
c.imprimir_coordenadas()
c.mover()
c.calcular_distancia()