# Estructuras de datos base del blog, este módulo solo guarda datos.

# Diccionario llamado perfil_autor
perfil_autor: dict[str, str | list[str]] = {
    "nombre": "Gabriela Maza Sasiuk",
    "bio": "Administradora de sistemas de gestión en el sector salud, en camino a Data Engineer.",
    "especialidad": "Java, SQL y datos",
    "redes_sociales": ["@gmaza_dev", "@gmaza_python"]
}

# Tupla llamada estados_post
estados_post: tuple[str, ...] = ("borrador", "publicado", "archivado")

# Tupla extra llamada categorias_blog
categorias_blog: tuple[str, ...] = ("Programación", "Datos", "Desarrollo web")

# Set llamado etiquetas_blog
etiquetas_blog: set[str] = {"Python", "SQL", "Datos", "Backend", "Django", "Web", "Principiantes", "Diccionarios"}

# Lista llamada posts
posts: list[dict] = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "categoria": categorias_blog[0],
        "tags": ["Python", "Principiantes"],
        "estado": estados_post[1]
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "categoria": categorias_blog[2],
        "tags": ["Python", "Django", "Web"],
        "estado": estados_post[0]
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Los diccionarios permiten guardar datos como pares clave-valor.",
        "autor": perfil_autor,
        "categoria": categorias_blog[0],
        "tags": ["Python", "Diccionarios"],
        "estado": estados_post[2]
    },
    # Post inválido: le falta el contenido
    {
        "id": 4,
        "titulo": "Consultas básicas en SQL",
        "autor": perfil_autor,
        "categoria": categorias_blog[1],
        "tags": ["SQL", "Datos"],
        "estado": estados_post[1]
    },
    # Post inválido: le falta el título, tags no es una lista y el estado no existe
    {
        "id": 5,
        "contenido": "Todo sobre Microsoft Access",
        "autor": perfil_autor,
        "categoria": categorias_blog[1],
        "tags": "Backend",
        "estado": "eliminado"
    }
]
