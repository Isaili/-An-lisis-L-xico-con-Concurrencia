import asyncio
import aiofiles
from lexer import Lexer



async def process_file(file_path):
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
        text = await f.read()
    lexer = Lexer(text)
    return lexer.tokenize()

async def run_asyncio(files):
    tasks = [process_file(file) for file in files]
    results = await asyncio.gather(*tasks)
    return [token for sublist in results for token in sublist]

if __name__ == "__main__":
    files = ["input/file1.txt", "input/file2.txt"]
    tokens = asyncio.run(run_asyncio(files))
    print("Tokens asyncio:", tokens)
