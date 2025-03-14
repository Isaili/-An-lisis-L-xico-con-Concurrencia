import re

# Definición de los tokens usando expresiones regulares
TOKEN_PATTERNS = [
    (r'\bint\b|\bfloat\b|\bif\b|\belse\b', 'KEYWORD'),  # Palabras clave
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  # Identificadores
    (r'\d+\.\d+', 'FLOAT'),  # Números flotantes
    (r'\d+', 'NUMBER'),  # Números enteros
    (r'==|!=|<=|>=|<|>', 'COMPARISON'),  # Operadores de comparación
    (r'[+\-*/=]', 'OPERATOR'),  # Operadores aritméticos
    (r'[();{}]', 'DELIMITER'),  # Delimitadores
    (r'\s+', None),  # Ignorar espacios en blanco
]

class Lexer:
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = []
        index = 0
        while index < len(self.text):
            for pattern, token_type in TOKEN_PATTERNS:
                match = re.match(pattern, self.text[index:])
                if match:
                    value = match.group(0)
                    if token_type:  # Ignorar tokens vacíos
                        tokens.append((token_type, value))
                    index += len(value)
                    break
            else:
                raise ValueError(f"Token no reconocido en: {self.text[index:]}")  # Error si no coincide
        return tokens
