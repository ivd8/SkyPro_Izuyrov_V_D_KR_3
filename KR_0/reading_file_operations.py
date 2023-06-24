import json #Подключили библиотеку для чтения JSON файлов
from pprint import pprint #Подключили библиотеку для более читабельного варианта при выводе на экран переменной text

with open('operations.json', 'r', encoding='utf-8') as f:
    text = json.load(f)  # загнали все из файла в переменную
    pprint(text)  # вывели результат на экран
