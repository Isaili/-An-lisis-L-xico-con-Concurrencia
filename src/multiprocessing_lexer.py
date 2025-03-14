import multiprocessing
from src.utils import read_file
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import Lexer


def process_file(file_path, queue):
    text = read_file(file_path)
    print(f"📜 Texto procesado ({file_path}):", text)  # Debug
    
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    
    print(f"📝 Tokens generados ({file_path}):", tokens)  # Debug
    queue.put(tokens)


def run_multiprocessing(files):
    queue = multiprocessing.Queue()
    processes = []

    for file in files:
        p = multiprocessing.Process(target=process_file, args=(file, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = []
    while not queue.empty():
        results.extend(queue.get())

    return results

if __name__ == "__main__":
    files = ["input/file1.txt", "input/file2.txt"]
    tokens = run_multiprocessing(files)
    print("Tokens multiprocessing:", tokens)
