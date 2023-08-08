class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def calcular_perímetro(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        perimetro = 2 * (base + altura)
        print("Perímetro:", perimetro)

    def calcular_área(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        area = base * altura
        print("Área:", area)

    def es_cuadrado(self):
        base = abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)
        altura = abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)
        if base == altura:
            print("¡Es un cuadrado!")
        else:
            print("No es un cuadrado.")


esquina_sup_izq = Punto(1, 4)
esquina_inf_der = Punto(4, 6)

mi_rectángulo = Rectángulo(esquina_sup_izq, esquina_inf_der)
mi_rectángulo.calcular_perímetro()
mi_rectángulo.calcular_área()
mi_rectángulo.es_cuadrado()