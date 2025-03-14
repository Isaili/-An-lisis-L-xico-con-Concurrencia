🔹 Análisis Léxico con Concurrencia

Este proyecto implementa un analizador léxico que procesa archivos de código utilizando expresiones regulares, incorporando multiprocessing y asyncio para mejorar el rendimiento en la ejecución concurrente.


📌 1. Arquitectura del Sistema
El sistema sigue una arquitectura modular con los siguientes componentes:

Lexer (lexer.py): Analiza el texto fuente y lo convierte en una lista de tokens.
Módulo de Procesamiento (txt1.py): Gestiona la lectura de archivos y aplica concurrencia.
Multiprocessing: Divide la carga entre múltiples procesos para mejorar el rendimiento en archivos grandes.
Asyncio: Ejecuta tareas en paralelo de manera asíncrona, ideal para archivos pequeños.
