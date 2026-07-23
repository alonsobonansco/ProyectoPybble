from abc import ABC, abstractmethod

class PerfilUsuario:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.lista_logros = []

    def ganar_logro(self, logro_obj):
        self.lista_logros.append(logro_obj)
        print(f"🏆 ¡{self.username} desbloqueó: {logro_obj.nombre}!")


# Clase Abstracta
class Logro(ABC):
    def __init__(self, nombre, puntos_experiencia):
        self.nombre = nombre
        self.puntos_experiencia = puntos_experiencia

    @abstractmethod
    def obtener_detalle(self):
        pass


# Clases Hijaa
class LogroHistoria(Logro):
    def obtener_detalle(self):
        return f"[Historia] {self.nombre} (+{self.puntos_experiencia} XP) - Completando la campaña."


class LogroDesafio(Logro):
    def __init__(self, nombre, puntos_experiencia, dificultad):
        super().__init__(nombre, puntos_experiencia)
        self.dificultad = dificultad

    def obtener_detalle(self):
        return f"[Desafío {self.dificultad}] {self.nombre} (+{self.puntos_experiencia} XP)"