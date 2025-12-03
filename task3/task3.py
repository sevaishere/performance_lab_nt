# Задание 3

import json

def change_values_recursive(dictionary: dict, data: dict):
    if next(iter(dictionary)) == 'id':
        for id in data:
            if dictionary['id'] == id:
                dictionary['value'] = data[id]
                break
    for k, v in dictionary.items():
        if isinstance(v, dict):
            change_values_recursive(v, data)
        elif isinstance(v, list):
            for item in v:
                change_values_recursive(item, data)
    return dictionary

tests_path = input('Введите путь к файлу «tests.json»: ')
values_path = input('Введите путь к файлу «values.json»: ')
report_path = input('Введите путь к файлу «report.json»: ')

with open(tests_path, 'r') as file:
    tests_file = json.load(file)

with open(values_path, 'r') as file:
    values_file = json.load(file)

ids_with_values = {}
for row in values_file['values']:
    ids_with_values[row['id']] = row['value']

report = change_values_recursive(tests_file, ids_with_values)

with open(report_path, 'w') as file:
    json.dump(report, file, indent=2)