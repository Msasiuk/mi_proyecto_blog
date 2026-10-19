# Interacción con el usuario: muestra el menú y maneja los input().

def mostrar_menu() -> int | None:
    """Muestra el menú y retorna la opción elegida como número.
    Si el usuario escribe texto, retorna None en lugar de cerrar el programa."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        opcion = int(input("Qué deseas hacer? Elegí una opción: "))
        return opcion
    except ValueError:
        print("Tenés que ingresar un número del 1 al 5.")
        return None

def pedir_texto(mensaje: str) -> str | None:
    """Pide un texto al usuario. Retorna None si lo deja vacío."""
    texto = input(mensaje).strip()
    if texto == "":
        print("Ups, no escribiste nada")
        return None
    return texto
