# ligasJuegoPy

![logo](https://img.shields.io/badge/ligasJuegoPy-v0.1-blue) ![python](https://img.shields.io/badge/python-3.8%2B-yellow)

## Simulador de ligas visual y fácil

ligasJuegoPy es un pequeño proyecto en Python para simular competiciones de fútbol (ligas y copas). Genera resultados aleatorios y produce tablas y resúmenes para análisis o diversión.

---

**Características principales**

- Simulación de partidos con resultados aleatorios.
- Soporta ligas y copas (torneos eliminatorios).
- Interfaz en consola (`mainConsole.py`) y una interfaz gráfica mínima (`mainUI.py`).
- Datos de ejemplo en la carpeta `ligas/` y configuración de equipos en `equipos.json`.

---

**Requisitos**

- Python 3.8 o superior

Si usas la interfaz gráfica (`mainUI.py`), puede que el proyecto use módulos estándar o dependencias incluidas en la distribución (si no estás seguro, ejecuta el script y revisa los errores para instalar paquetes faltantes).

---

**Instalación y ejecución**

1. Clona o descarga el repositorio.
2. Abre una terminal en la carpeta del proyecto.

Para ejecutar la versión de consola:

```bash
python mainConsole.py
```

Para ejecutar la interfaz (ventana gráfica mínima):

```bash
python mainUI.py
```

En Windows puedes usar `py -3 mainConsole.py` si tienes varias versiones de Python.

O bien, puedes descargar el ejecutable ya compilado. Una vez descargado el archivo `.zip`, extraelo y dentro se encuentra un `.exe`.   

---

**Estructura del proyecto (resumen)**

- `equipos.json` - configuración / lista de equipos.
- `logica.py` - funciones centrales de simulación.
- `mainConsole.py` - interfaz por consola para ejecutar simulaciones.
- `mainUI.py` - interfaz gráfica.
- `UISupportModule.py` - utilidades para la UI (creadas con PAGE).
- `classModel/` - modelos de dominio (clases `Equipo`, `Liga`, `Copa`, `Confederacion`, etc.).
- `ligas/` - datos de ejemplo (resultados, históricos).

---

**Cómo usar (ejemplos)**

- Ejecutar una simulación completa en consola: `python mainConsole.py`- sigue las opciones interactivas.
- Abrir la UI: `python mainUI.py` - si la UI no arranca revisa la salida para instalar dependencias.
- Revisar datos de salida en la carpeta `ligas/` y archivos generados.

---

**Consejos y notas**

- Para ver y modificar equipos, edita `equipos.json`.
- Para cambiar la lógica de simulación, editar `logica.py` y las clases en `classModel/`.


