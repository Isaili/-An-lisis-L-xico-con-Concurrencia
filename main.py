import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.lexer import Lexer
from src.utils import read_file
from src.multiprocessing_lexer import run_multiprocessing
from src.asyncio_lexer import run_asyncio
import asyncio

def main():
    files = ["input/file1.txt", "input/file2.txt"]

    # Multiprocessing
    print("\nEjecutando análisis con multiprocessing...")
    tokens_mp = run_multiprocessing(files)
    print("Tokens multiprocessing:", tokens_mp)

    # Asyncio
    print("\nEjecutando análisis con asyncio...")
    tokens_async = asyncio.run(run_asyncio(files))
    print("Tokens asyncio:", tokens_async)

if __name__ == "__main__":
    main()
