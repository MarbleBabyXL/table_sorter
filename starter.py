import time
from pathlib import Path
import pandas as pd
import os

script_path = str(Path(__file__).resolve())
#10
pth = rf"{script_path[:-10]}working-directory"
cfg = rf"{script_path[:-10]}config.txt"
print(pth+"\n"+cfg)
files = rf"{pth}\{os.listdir(pth)[0]}"
print(files)

def reader(content):
    try:
        df = pd.read_excel(files, sheet_name=content[0])
        name_of_sheet = content[0]
        name_of_sheet = name_of_sheet[0]
        a = content[1]
        a = a[0]
        data_frame = df[name_of_sheet]
        columns_to_delete = a.split("/")
        for i in columns_to_delete:
            data_frame.drop(columns=i, inplace=True, errors='ignore')
        data_frame.to_excel(f'{pth}/modified_file.xlsx', index=False, engine='openpyxl')

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def read_cfg():
    try:
        with open(cfg, 'r', encoding='utf-8') as f:
            config_data = f.readlines()

        sheet_names = []
        column_names = []
        for line in config_data:
            if 'name_of_sheet=' in line:
                sheet_names.append(line.split('=')[1].strip())
            elif 'name_of_columns=' in line:
                column_names.append(line.split('=')[1].strip())
        result_array = [sheet_names, column_names]
        return result_array
    except Exception as e:
        print(f"Произошла ошибка: {e}")


cnt = read_cfg()
reader(cnt)
print(cnt)
time.sleep(1000)