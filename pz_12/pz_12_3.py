"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

yaml_data = {"items": ["computer", "printer", "keyboard", "mouse"],
             "items_quantity": 4,
             "items_ptice": {"computer": "200€-1000€", "keyboard": "5€-50€",
                             "mouse": "4€-7€", "printer": "100€-300€"}}
with open("file.yaml", "w", encoding="utf-8") as yaml_file:
    yaml.dump(yaml_data, yaml_file, default_flow_style=False,
              allow_unicode = True, sort_keys=False)

with open("file.yaml", "r", encoding="utf-8") as yaml_file:
    print(yaml_file.read())

with open("file.yaml", "r", encoding="utf-8") as yaml_file:
    yaml_content = yaml.load(yaml_file, Loader=yaml.SafeLoader)
print(yaml_content == yaml_data)


