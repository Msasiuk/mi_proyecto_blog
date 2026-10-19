# main.py
# Archivo principal: importa las piezas del paquete blog y coordina el flujo del menú.

from blog.datos import posts, etiquetas_blog
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import (
    listar_posts,
    buscar_por_titulo,
    filtrar_por_tag,
    mostrar_resultados,
    mostrar_validacion,
)


def main() -> None:
    """Inicia el blog y coordina el menú hasta que el usuario elige salir."""
    print("Hola! Bienvenid@ a nuestro blog de Programación.")
    while True:
        opcion = mostrar_menu()

        # Si se ingresó texto, se vuelve a mostrar el menú
        if opcion is None:
            continue

        # Opción 1: Ver todos los posts
        if opcion == 1:
            listar_posts(posts)

        # Opción 2: Buscar por titulo
        elif opcion == 2:
            termino = pedir_texto("Qué título estás buscando? ")
            if termino is not None:
                print("\nResultados de tu búsqueda:")
                encontrados = buscar_por_titulo(posts, termino)
                mostrar_resultados(encontrados, "Ups, no encontramos ningún post con ese título.")

        # Opción 3: Filtrar por tag
        elif opcion == 3:
            print("Tags disponibles:", ", ".join(sorted(etiquetas_blog)))
            tag = pedir_texto("Por cuál tag quieres navegar? ")
            if tag is not None:
                print(f"\nPosts con el tag '{tag}':")
                filtrados = filtrar_por_tag(posts, tag)
                mostrar_resultados(filtrados, "Ups, no encontramos ningún post con ese tag.")

        # Opción 4: Validar posts
        elif opcion == 4:
            mostrar_validacion(posts)

        # Opción 5: Salir
        elif opcion == 5:
            print("Gracias por pasar! Nos vemos pronto.")
            break

        # Número fuera del menú
        else:
            print("Esa opción no existe. Elegí un número del 1 al 5.")


if __name__ == "__main__":
    main()
