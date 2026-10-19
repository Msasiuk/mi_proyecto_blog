# mi_proyecto_blog

Sistema de blog por consola desarrollado en el curso de Python de Coderhouse.
Permite listar posts, buscar por título, filtrar por tag y validar la estructura de cada publicación.

En esta versión (Preentrega 5) el sistema se reorganizó en un paquete con  móduls, cada uno con una responsabilidad. Además las funciones y los datos base tienen **type hints** (anotaciones de tipo) para que el código sea más fácil de leer.

## Requisitos

- Python 3.10 o superior (por la sintaxis de type hints como `int | None`). 

## Cómo ejecutarlo

1. Abrí una terminal (CMD en Windows) y ubicate en la carpeta raíz del proyecto, donde está `main.py`:

   ```
   cd mi_proyecto_blog
   ```

2. Ejecutá el archivo principal:

   ```
   python main.py
   ```

3. Elegí una opción del menú escribiendo un número del 1 al 5.

## Estructura del proyecto

```
mi_proyecto_blog/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Archivo principal. Importa las funciones del paquete `blog` y coordina el flujo del menú en la función `main()`, que se ejecuta dentro de `if __name__ == "__main__":`. |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog` como un paquete. |
| `blog/datos.py` | Datos base del blog: `perfil_autor`, `estados_post`, `categorias_blog`, `etiquetas_blog` y `posts`. |
| `blog/menu.py` | Interacción con el usuario: `mostrar_menu()` (con `try-except`) y `pedir_texto()`. |
| `blog/operaciones.py` | Funciones del blog: `listar_posts(lista)`, `buscar_por_titulo(lista, termino)`, `filtrar_por_tag(lista, tag)`, `mostrar_resultados(...)` y `mostrar_validacion(lista)`. |
| `blog/validaciones.py` | Reglas lógicas: `validar_post(post)` y las claves obligatorias de un post. |

Los imports van en una sola dirección para evitar imports circulares:

```
main.py → menu, operaciones, datos
operaciones.py → validaciones.py → datos.py
```

## Type hints

Cada función indica qué tipo de dato recibe y qué devuelve. Por ejemplo:

```python
def buscar_por_titulo(lista: list[dict], termino: str) -> list[dict]:
def validar_post(post: dict) -> tuple[bool, str]:
def mostrar_menu() -> int | None:
```

Los type hints no cambian cómo funciona el programa: sirven como documentación y ayudan al editor (VS Code) a detectar errores.

## Opciones del menú

1. **Ver todos los posts**: muestra título, autor y estado de cada publicación. Los posts con errores aparecen como "Post inválido".
2. **Buscar por titulo**: busca posts cuyo título contenga el término, sin importar mayúsculas (usa `.lower()`). Solo muestra posts válidos.
3. **Filtrar por tag**: muestra los posts que tienen ese tag, sin importar mayúsculas (usa `.lower()`). Solo muestra posts válidos.
4. **Validar posts**: indica qué posts son válidos y qué error tiene cada uno de los que no.
5. **Salir**: termina el programa.

## Reglas de validación

Todos los campos son obligatorios: `id`, `titulo`, `contenido`, `autor`, `categoria`, `tags` y `estado`. Además:

- El título y el contenido no pueden estar vacíos.
- El autor debe ser un diccionario con la clave `nombre`.
- La categoría debe pertenecer a `categorias_blog`.
- Los tags deben ser una lista.
- El estado debe pertenecer a `estados_post`.

La lista incluye dos posts con errores a propósito (uno sin contenido y otro sin título, con tags como texto y estado inválido) para probar la validación. Por eso, al filtrar por el tag `SQL` no aparecen resultados: el único post con ese tag es inválido y se excluye.

