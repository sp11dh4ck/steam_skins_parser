import os
from config import s

folder_path = f'{s}'
filename = 'skins.txt'

if not os.path.exists(folder_path):
    print(f'Папка {folder_path} не существует.')
    exit()

if not os.path.isfile(filename):
    print(f'Файл {filename} не существует.')
    exit()

with open(filename, 'r') as file:
    names = file.readlines()

files = os.listdir(folder_path)
sorted_list = sorted(files, key=lambda x: int(x.split('.')[0]))

if len(names) != len(sorted_list):
    print("\033[31m{}".format('Количество файлов и имен не совпадает.'))
    exit()

for i in range(len(sorted_list)):
    old_file_name = sorted_list[i]
    new_file_name = names[i].strip() + '.png'
    
    old_file_path = os.path.join(folder_path, old_file_name)
    new_file_path = os.path.join(folder_path, new_file_name)
    
    os.rename(old_file_path, new_file_path)
    
    print("\033[32m{}".format(f'Файл {old_file_name} переименован в {new_file_name}'))
