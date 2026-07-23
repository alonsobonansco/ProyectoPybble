class Juego:
    # Constructor de Juego
    def __init__(self, titulo, genero, precio_base):
        self.titulo = titulo
        self.genero = genero
        self.precio_base = precio_base

    def obtener_formato(self):
        return "Físico / Estándar"

# Subclase de Juego
class JuegoDigital(Juego):
    def __init__(self, titulo, genero, precio_base, tamano_gb, plataforma):
        super().__init__(titulo, genero, precio_base)
        self.tamano_gb = tamano_gb
        self.plataforma = plataforma

    def obtener_formato(self):
        return f"Digital ({self.plataforma} - {self.tamano_gb} GB)"