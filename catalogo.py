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

class Biblioteca:
    def __init__(self):
        # Diccionario para asociar un Objeto Juego con sus Horas Jugadas
        # Estructura: { objeto_juego: int_horas }
        self.mis_juegos = {}

    def agregar_juego(self, juego_obj):
        if juego_obj not in self.mis_juegos:
            self.mis_juegos[juego_obj] = 0

    def registrar_horas(self, juego_obj, horas):
        if juego_obj in self.mis_juegos:
            self.mis_juegos[juego_obj] += horas

    def calcular_tiempo_total(self):
        return sum(self.mis_juegos.values())