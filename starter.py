import pandas as pd
import os

script_path = os.path.abspath(__file__)
pth = rf"{script_path[:-10]}working-directory"
cfg = rf"{script_path[:-10]}config.txt"
files = rf"{pth}\{os.listdir(pth)[0]}"

def reader(content):
    try:
        df = pd.read_excel(files, sheet_name="Лист 1")
        columns = []
        for a in content:
            columns.append(a)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def read_info():
    try:
        with open(cfg, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"По расположению '{cfg}' файл не найден."
    except IOError:
        return "Ошибка при чтении файла."


cnt = read_info()
reader(cnt)
print(cnt)