# Programación en Python · Repositorio del alumnado

Apuntes y autoevaluación de la materia de programación con Python, en formato [MkDocs](https://www.mkdocs.org/) (tema Material).
Sirve tanto para el estudio individual como para las explicaciones en clase.

**Unidades disponibles:** UT01 y UT02.

## Ver los apuntes

```bash
# 1. (Una sola vez) crear un entorno virtual e instalar las dependencias
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS
pip install -r requirements.txt

# 2. Servidor local con recarga automática
mkdocs serve                    # abre http://127.0.0.1:8000
```

### Generar una versión que funciona sin conexión

```bash
mkdocs build
```

Se crea la carpeta `site/`. Como el tema no descarga fuentes y las URL son relativas,
puedes abrir `site/index.html` directamente con el navegador, sin servidor y sin conexión.

> El buscador del sitio es más fiable con `mkdocs serve`. Al abrir los archivos directamente desde el disco,
> algunos navegadores pueden necesitar conexión para cargar un pequeño componente auxiliar del buscador (el resto del sitio funciona sin ella).

## Estructura

```
mkdocs.yml            configuración del sitio y menú de navegación
requirements.txt      dependencias
docs/
├── index.md          portada y guía de uso
├── evaluacion.md     cómo se evalúa la materia
├── ut01/             apuntes (a–h) + autoevaluación
└── ut02/             apuntes (a–d) + autoevaluación
```

Cada unidad termina con una página de **autoevaluación** (preguntas, ejercicios y un proyecto de práctica) que incluye las soluciones,
ocultas hasta que las despliegues.

## Añadir una unidad nueva

1. Crea la carpeta `docs/utNN/` con una página por apartado y una `autoevaluacion.md`.
2. Añádela al bloque `nav` de `mkdocs.yml`.
3. Comprueba con `mkdocs build --strict` que no hay enlaces rotos.
