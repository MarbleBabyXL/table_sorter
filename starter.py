import pandas as pd
import os

script_path = os.path.abspath(__file__)
pth = rf"{script_path[:-10]}working-directory"
cfg = rf"{script_path[:-10]}config.txt"
files = rf"{pth}\{os.listdir(pth)[0]}"

def reader(content):
    try:
        df = pd.read_excel(files, sheet_name=content[0])
        print(f"Тип загруженных данных: {type(df)}")
        a = content[1]
        a = a[0]
        columns_to_delete = a.split("/")
        for i in columns_to_delete:
            df.drop(columns=i, inplace=True, errors='ignore')
        df.to_excel(f'{pth}/modified_file.xlsx', index=False, engine='openpyxl')

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def read_cfg():
    with open('config.txt', 'r', encoding='utf-8') as f:
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


cnt = read_cfg()
reader(cnt)
print(cnt)