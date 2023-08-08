class Carta:
    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    PICA = "Pica"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta


carta1 = Carta(2, Carta.CORAZON)
print("Valor:", carta1.valor, "Pinta:", carta1.pinta)
