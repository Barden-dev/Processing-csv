# Обработка csv файла

## Пошаговая инструкция:

**Склонируйте репозиторий:**
```
git clone https://github.com/Barden-dev/Processing-csv.git
cd Processing-csv
```


### **Создайте и активируйте виртуальное окружение:**
#### Для Linux / macOS
```
python3 -m venv venv
source venv/bin/activate
```
#### Для Windows
```
python -m venv venv
.\venv\Scripts\activate
```


**Установите зависимости:**
```
pip install -r requirements.txt
```

## Использование
1. Вывод всей таблицы:

```
python main.py --file data/products.csv
```
2. Фильтрация по бренду:

```
python main.py --file data/products.csv --where "brand=apple"
```
3. Фильтрация по цене:

```
python main.py --file data/products.csv --where "price>700"
```

4. Сортировка по цене (по убыванию):
```
python main.py --file data/products.csv --order-by "price=desc"
```

5. Агрегация (средний рейтинг всех товаров):
```
python main.py --file data/products.csv --aggregate "rating=avg"
```

6. Комбинация всех операций:
Найти среднюю цену на телефоны Samsung, предварительно отсортировав их по рейтингу.
```
python main.py --file data/products.csv --where "brand=samsung" --order-by "rating=desc" --aggregate "price=avg"
```

### 🧪 Тестирование
Проект покрыт тестами с использованием pytest.

1. Запуск всех тестов:
Выполните команду из корневой папки проекта.

```
pytest
```
2. Запуск тестов с отчётом о покрытии:

```
pytest --cov=processing_csv
```
