# 🔹 Análisis Léxico con Concurrencia

Este proyecto implementa un analizador léxico que procesa archivos de código utilizando expresiones regulares, incorporando multiprocessing y asyncio para mejorar el rendimiento en la ejecución concurrente.

## 📌 1. Arquitectura del Sistema
El sistema sigue una arquitectura modular con los siguientes componentes:

- 🌫**Lexer (lexer.py):** Analiza el texto fuente y lo convierte en una lista de tokens.
- ⛈**Módulo de Procesamiento (txt1.py): **Gestiona la lectura de archivos y aplica concurrencia.
- 💧**proceso_pluvial.py**: Simula el llenado desde la fuente pluvial.
- 🎊**pMultiprocessing:y**: Divide la carga entre múltiples procesos para mejorar el rendimiento en archivos grandes.
- 🎍**Asyncio:**: Ejecuta tareas en paralelo de manera asíncrona, ideal para archivos pequeños.

## 🗂️ 2. Estructura del Proyecto

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

#### 📌 3. Estrategia de Concurrencia
1. **multiprocessing**:
  - Se usa multiprocessing.Pool() para ejecutar el análisis en múltiples archivos simultáneamente.
  - Ideal para grandes volúmenes de texto o múltiples archivos grandes

2. **Asyncio:**:
  - Se usa asyncio.to_thread() para ejecutar el análisis en paralelo sin bloquear el proceso principal.
  - Funciona mejor en escenarios donde hay múltiples archivos pequeños.
  
---

## 🚀 4. Instalación y Ejecución

**🔹 Requisitos**
- Python 3.x
- Librerías estándar de Python (re, asyncio, multiprocessing, os)

### 1⃣  Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/proyecto_lexer.git
cd proyecto_lexer

```

### 2⃣  Ejecutar la aplicación
```bash
python main.py
```
---
