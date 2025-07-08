import argparse

from tabulate import tabulate
from processing_csv.data_handler import load_data_from_csv
from processing_csv.logic_handler import proccess_data


parser = argparse.ArgumentParser(description="Скрипт для обработки данных из CSV файла. \n Есть возможность использования нескольких аргументов сразу")
parser.add_argument(
    "-f",
    "--file",
    default="data/products.csv",
    type=str,
    help="Обязательный аргумент: путь к CSV файлу."
    )
parser.add_argument(
    "-w",
    "--where",
    type=str,
    help= f"Необязательный аргумент: Фильтр данных. Формат: \"столбец=значение\". Например: main.py -f data.csv -w \"brand=apple\""
    )
parser.add_argument(
    "-a",
    "--aggregate",
    type=str,
    help= f"Необязательный аргумент: Агрегация данных. Формат: \"столбец=функция\". Доступные функции: avg, max, min, med.  Например: main.py -f data.csv -a \"rating=avg\""
    )
parser.add_argument(
    "-o-by",
    "--order-by",
    type=str,
    help= f"Необязательный аргумент: Сортировка дынных. Формат: \"столбец=функция\". Доступные функции: asc, desc. Например: main.py -f data.csv --order-by \"rating=desc\""
    )
args = parser.parse_args()


if __name__ == "__main__":
    data = load_data_from_csv(args.file)
    if data is None:
        print("Ошибка при загрузке данных, файла не существует. Проверьте, правильно ли указан путь. Стандартный путь: data/products.csv")
    else:
        result = proccess_data(data, args)
        if result:
            print(tabulate(result, headers="firstrow", tablefmt="grid"))