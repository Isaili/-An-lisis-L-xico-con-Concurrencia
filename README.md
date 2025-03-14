# 🔹 Análisis Léxico con Concurrencia

Este proyecto implementa un analizador léxico que procesa archivos de código utilizando expresiones regulares, incorporando multiprocessing y asyncio para mejorar el rendimiento en la ejecución concurrente.

## 📌 1. Arquitectura del Sistema
El sistema sigue una arquitectura modular con los siguientes componentes:

- 🌫**Lexer (lexer.py):** Analiza el texto fuente y lo convierte en una lista de tokens.
- ⛈**Módulo de Procesamiento (txt1.py): **Gestiona la lectura de archivos y aplica concurrencia.
- 💧**proceso_pluvial.py**: Simula el llenado desde la fuente pluvial.
- 🎊**pMultiprocessing:y**: Divide la carga entre múltiples procesos para mejorar el rendimiento en archivos grandes.
- 🎍**Asyncio:**: Ejecuta tareas en paralelo de manera asíncrona, ideal para archivos pequeños.

## 🗂️ Estructura del Proyecto

```bash
LSO/
 ├── 📁 .venv
 ├── 📁 .input
 ├── 📁 .output
 ├── 📁 .src
    ├── 📁 __pycache__   # cache de los archivos
    ├── 🗍 __init__.py   
    ├── 🗍 asyncio_lexer.py    # Scripts de fuentes y consumos
    ├── 🗍 gui.py    # Scripts de fuentes y consumos        
    ├── 🗍 lexer.py    # Scripts de fuentes y consumos
    ├── 🗍 multiprocessing_lexer.py    # Scripts de fuentes y consumos
    ├── 🗍 utils.py   # Scripts de fuentes y consumos
  ├── 📁 test
    ├── 🗍 test_lexer.py
  ├── 🗍 main   
  ├── 🗍 README.md    # Documentación
 
```
---
