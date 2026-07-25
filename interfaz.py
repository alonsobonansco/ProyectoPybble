import customtkinter as ctk

from catalogo import JuegoDigital, Biblioteca, Juego
from usuarios import PerfilUsuario

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class AppBiblioteca(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registro de juegos definitivo")
        self.geometry("600x500")
        self.resizable(False, False)

        self.usuario = PerfilUsuario("ElAmigoB", "asdf@gmail.com")
        self.biblioteca = Biblioteca()

        self.juego1 = JuegoDigital("Elden Ring", "Action RPG", 59.99, 60, "Steam")
        self.juego2 = JuegoDigital("Hollow Knight", "Metroidvania", 14.99, 9, "Switch")
        self.biblioteca.agregar_juego(self.juego1)
        self.biblioteca.agregar_juego(self.juego2)

        self.label_titulo = ctk.CTkLabel(
            self,
            text=f"Biblioteca de {self.usuario.username}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.label_titulo.pack(pady=20)

        self.txt_pantalla = ctk.CTkTextbox(self, width=500, height=200, font=ctk.CTkFont(size=13))
        self.txt_pantalla.pack(pady=10)

        self.actualizar_lista_juegos()

        self.btn_jugar_elden = ctk.CTkButton(
            self,
            text="Jugar 2 horas a Elden Ring",
            command=self.acc_jugar_elden_ring
    )

        self.btn_jugar_elden.pack(pady=10)

        self.btn_jugar_hollow = ctk.CTkButton(
            self,
            text="Jugar 1 hora a Hollow Knight",
            command=self.acc_jugar_hollow_knight
    )

        self.btn_jugar_hollow.pack(pady=10)

        self.label_horas = ctk.CTkLabel(
            self,
            text=f"Tiempo total jugado: {self.biblioteca.calcular_tiempo_total()} horas",
            font=ctk.CTkFont(size=14, weight="bold")
    )
        self.label_horas.pack(pady=20)

    def actualizar_lista_juegos(self):
        """Limpia el cuadro de texto y vuelve a listar los juegos con sus datos"""
        self.txt_pantalla.delete("0.0", "end")

        texto_acumulado = "Juegos en tu colección:\n"
        texto_acumulado += "-" * 50 + "\n"

        for juego, horas in self.biblioteca.mis_juegos.items():
            texto_acumulado += f"• {juego.titulo} [{juego.genero}]\n"
            texto_acumulado += f"  Formato: {juego.obtener_formato()}\n"
            texto_acumulado += f"  Tiempo registrado: {horas} horas\n\n"

        self.txt_pantalla.insert("0.0", texto_acumulado)

    def acc_jugar_elden_ring(self):
        """Acción al presionar el botón de Elden Ring"""
        self.biblioteca.registrar_horas(self.juego1, 2)
        self.label_horas.configure(text=f"Tiempo total jugado: {self.biblioteca.calcular_tiempo_total()} horas")
        self.actualizar_lista_juegos()

    def acc_jugar_hollow_knight(self):
        """Acción al presionar el botón de Hollow Knight"""
        self.biblioteca.registrar_horas(self.juego2, 1)
        self.label_horas.configure(text=f"Tiempo total jugado: {self.biblioteca.calcular_tiempo_total()} horas")
        self.actualizar_lista_juegos()


if __name__ == "__main__":
    app = AppBiblioteca()
    app.mainloop()
