import os
import json

# Указываем путь к директории
directory = "/Users/RossokhinDO/Downloads/tests/_output/allure-results/"

# Создаем пустой список
files = []

# Добавляем файлы в список
files += os.listdir(directory)
data = []

for i in files:
    with open('/Users/RossokhinDO/Downloads/tests/_output/allure-results/'+i) as f:
        templates = json.load(f)
        # if 'children' in templates:
        #     if '11f05902-cb86-480c-8adb-111bdbda78a2' in templates['children']:
        #         print(i)
        data.append(templates)

with open('sw_templates.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)