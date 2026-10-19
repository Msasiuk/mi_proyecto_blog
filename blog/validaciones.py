# Reglas lógicas: verifica que cada post tenga la estructura correcta.

from blog.datos import estados_post, categorias_blog

# Claves que todo post debe tener para ser válido (todas son obligatorias)
claves_obligatorias: tuple[str, ...] = ("id", "titulo", "contenido", "autor", "categoria", "tags", "estado")

def validar_post(post: dict) -> tuple[bool, str]:
    """Verifica que el post cumpla las reglas del blog.
    Retorna (True, "válido") o (False, "mensaje con el error")."""
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    # Que existan las claves obligatorias
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    # Que el título no esté vacío
    titulo = post.get("titulo")
    if not isinstance(titulo, str) or titulo.strip() == "":
        return False, "el título está vacío"

    # Que el contenido no esté vacío
    contenido = post.get("contenido")
    if not isinstance(contenido, str) or contenido.strip() == "":
        return False, "el contenido está vacío"

    # Que el autor sea un diccionario con la clave "nombre"
    autor = post.get("autor")
    if not isinstance(autor, dict):
        return False, "el autor no es un diccionario"
    if "nombre" not in autor:
        return False, 'el autor no tiene la clave "nombre"'

    # Que la categoría sea una de las definidas en categorias_blog
    if post.get("categoria") not in categorias_blog:
        return False, f'la categoría "{post.get("categoria")}" no es válida'

    # Que tags sea una lista
    if not isinstance(post.get("tags"), list):
        return False, "tags no es una lista"

    # Que el estado sea uno de los definidos en estados_post
    if post.get("estado") not in estados_post:
        return False, f'el estado "{post.get("estado")}" no es válido'
    return True, "válido"
