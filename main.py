from usuarios import PerfilUsuario, LogroHistoria, LogroDesafio
from catalogo import JuegoDigital, Biblioteca


def ejecutar_sistema():
    print("=== SISTEMA DE REGISTRO DE VIDEOJUEGOS ===")

    usuario = PerfilUsuario("PibbleLover", "pibblelover101@gmail.com")

    juego1 = JuegoDigital("Battlefield 6", "Accion", 59.99, 120, "Steam")
    juego2 = JuegoDigital("Left 4 Dead 2", "Accion/Terror", 11.99, 12, "Steam")

    biblioteca_personal = Biblioteca()
    biblioteca_personal.agregar_juego(juego1)
    biblioteca_personal.agregar_juego(juego2)

    biblioteca_personal.registrar_horas(juego1, 12)
    biblioteca_personal.registrar_horas(juego2, 5)
    biblioteca_personal.registrar_horas(juego1, 8)

    logro1 = LogroHistoria("Derrota a 10 enemigos", 250)
    logro2 = LogroDesafio("Completa el juego sin morir", 10000, "Extremo")

    print(f"\nSesión activa de: {usuario.username}")
    usuario.ganar_logro(logro1)
    usuario.ganar_logro(logro2)

    print("\n" + "=" * 35)
    print(" RESUMEN DE TU BIBLIOTECA ")
    print("=" * 35)

    print(f"Total de tiempo jugado: {biblioteca_personal.calcular_tiempo_total()} horas.")

    print("\nDetalle de Logros Obtenidos:")
    for logro in usuario.lista_logros:
        print(f" -> {logro.obtener_detalle()}")

if __name__ == "__main__":
    ejecutar_sistema()