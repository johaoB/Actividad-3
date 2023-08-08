import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        print("Área:", area)

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print("Perímetro:", perimetro)

    def punto_pertenece(self, punto):
        distancia = math.sqrt((punto[0] - self.centro[0])**2 + (punto[1] - self.centro[1])**2)
        if distancia <= self.radio:
            print("El punto", punto,"pertenece al circulo")
        else:
            print("El punto", punto, "no pertenece al circulo")


centro = (0, 0)
radio = 5
mi_circulo = Circulo(centro, radio)

mi_circulo.calcular_area()
mi_circulo.calcular_perimetro()

punto1 = (3, 4)
punto2 = (6, 6)
mi_circulo.punto_pertenece(punto1)
mi_circulo.punto_pertenece(punto2)
