def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"📂 Contenido leído ({file_path}):", repr(content))  # Depuración
        return content
    except Exception as e:
        print(f"⚠️ Error al leer {file_path}: {e}")
        return ""
