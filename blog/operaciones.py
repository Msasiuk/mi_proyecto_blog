# Funciones del blog: listar, buscar y filtrar posts.

from blog.validaciones import validar_post

def obtener_nombre_autor(post: dict) -> str:
    """Devuelve el nombre del autor de forma segura."""
    autor = post.get("autor")
    if isinstance(autor, dict):
        return autor.get("nombre", "Autor desconocido")
    return "Autor desconocido"

def mostrar_post(post: dict) -> None:
    """Muestra título, autor y estado solo si el post es válido.
    Si tiene errores, no muestra sus datos y avisa que es inválido."""
    es_valido, mensaje = validar_post(post)
    if es_valido:
        print("-", post.get("titulo"), "| Autor:", obtener_nombre_autor(post), "| Estado:", post.get("estado"))
    else:
        print(f"- Post {post.get('id', '?')}: Post inválido ({mensaje})")

def mostrar_resultados(resultados: list[dict], mensaje_vacio: str) -> None:
    """Muestra los posts encontrados o un mensaje si no encuentra resultados."""
    if resultados:
        for post in resultados:
            mostrar_post(post)
    else:
        print(mensaje_vacio)

def listar_posts(lista: list[dict]) -> None:
    """Recorre la lista de posts y muestra título, autor y estado."""
    if not lista:
        print("Todavía no hay posts por acá.")
        return
    print("\nPosts disponibles:")
    for post in lista:
        if isinstance(post, dict):
            mostrar_post(post)
        else:
            print("- Hay un registro que no es un post válido")

def buscar_por_titulo(lista: list[dict], termino: str) -> list[dict]:
    """Retorna una lista con los posts válidos cuyo título contiene el término ingresado.
    La búsqueda no distingue mayúsculas de minúsculas. Los posts inválidos se ignoran."""
    resultados: list[dict] = []
    termino = termino.lower()
    for post in lista:
        # Si el post no es válido, no se incluye en la búsqueda
        es_valido, _ = validar_post(post)
        if not es_valido:
            continue
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino in titulo.lower():
            resultados.append(post)
    return resultados

def filtrar_por_tag(lista: list[dict], tag: str) -> list[dict]:
    """Retorna una lista con los posts válidos que tienen el tag indicado.
    La búsqueda no distingue mayúsculas de minúsculas. Los posts inválidos se ignoran."""
    resultados: list[dict] = []
    tag = tag.lower()
    for post in lista:
        # Si el post no es válido, no se incluye en el filtrado
        es_valido, _ = validar_post(post)
        if not es_valido:
            continue
        tags = post.get("tags", [])
        # Si tags no es una lista, el post se ignora
        if isinstance(tags, list):
            for t in tags:
                if str(t).lower() == tag:
                    resultados.append(post)
                    break
    return resultados

def mostrar_validacion(lista: list[dict]) -> None:
    """Recorre los posts y muestra cuáles son válidos y qué error tiene cada inválido."""
    print("\nValidación de posts")
    for numero, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        if es_valido:
            print(f"Post {numero}: válido")
        else:
            print(f"Post {numero}: inválido - {mensaje}")