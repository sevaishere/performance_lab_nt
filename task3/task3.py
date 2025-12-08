# Задание 3

import sys, json

def args_check(numb_of_args: int, args_rules: str):
    args_len = len(sys.argv[1:])
    if args_len < 1:
        sys.exit('Не введено ни одного аргумента.\n' + args_rules)
    elif args_len < numb_of_args:
        sys.exit('Введено слишком мало аргументов.\n' + args_rules)
    elif args_len > numb_of_args:
        sys.exit('Введено слишком много аргументов.\n' + args_rules)

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

args_check(3, 'В качестве аргументов необходимо последовательно ввести пути к файлам: '
              '«tests.json», «values.json» и «report.json» (всего 3 аргумента).')

tests_path = sys.argv[1]
values_path = sys.argv[2]
report_path = sys.argv[3]

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

print('По указаному вами пути создан файл «report.json».')