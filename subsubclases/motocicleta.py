from subclases.coche import Coche

class Motocicleta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas, velocidad, cilindrada)
