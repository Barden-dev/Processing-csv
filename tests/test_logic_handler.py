import pytest
import argparse

from processing_csv.logic_handler import proccess_data

@pytest.mark.parametrize(
    "where_arg, aggregate_arg, order_by_arg, expected_result",
    [
        #ДАННЫЕ ДЛЯ ТЕСТИРОВАНИЯ ФИЛЬТРА НАЧАЛО
        (
            "name=iphone", 
            None,
            None,
            [['name', 'brand', 'price', 'rating'], 
            ['iphone', 'apple', '999', '4.9']]
        ),
        
        (
            "rating=4.6", 
            None,
            None,
            [['name', 'brand', 'price', 'rating'], 
            ['redmi note 12', 'xiaomi', '199', '4.6'],
            ['galaxy z flip 5', 'samsung', '999', '4.6']]
        ),
        
                (
            "brand=apapappa", #Таких данных нет
            None,
            None,
            [['name', 'brand', 'price', 'rating']]
        ),
        
        ( 
            "count=2000", #Столбца не существует 
            None,
            None,
            None
        ),
        (
            "brand apple", #Неправильно прописан аргумент
            None,
            None,
            None
        ),
        #ДАННЫЕ ДЛЯ ТЕСТИРОВАНИЯ ФИЛЬТРА КОНЕЦ
        
        
        #ДАННЫЕ ДЛЯ ТЕСТИРОВАНИЯ СОРТИРОВКИ НАЧАЛО
        (
            "brand=xiaomi", 
            None,
            "name=asc",
            [['name', 'brand', 'price', 'rating'],
            ['poco x5 pro', 'xiaomi', '299', '4.4'], 
            ['redmi 10c', 'xiaomi', '149', '4.1'], 
            ['redmi note 12', 'xiaomi', '199', '4.6']]
        ),
        
        (
            None, 
            None,
            "count=desc", #Столбца не существует 
            None
        ),
        
        (
            None, 
            None,
            "rating asc", #Неправильно прописан аргумент
            None
        ),
        #ДАННЫЕ ДЛЯ ТЕСТИРОВАНИЯ СОРТИРОВКИ КОНЕЦ
        
        
        #ДАННЫЕ ДЛЯ ТЕСТИРОВАНИЯ АГРЕГАЦИИ НАЧАЛО
        (
            None,
            "price=avg",
            None,
            [['avg'], [686.5]]
        ),
        
        (
            None,
            "rating=min",
            None,
            [['min'], [4.1]]
        ),
        
        (
            None,
            "rating=max",
            None,
            [['max'], [5]]
        ),
        
        (
            None,
            "rating=med",
            None,
            [['med'], [4.6]]
        ),
        
        (
            "brand=apple",
            "rating=med",
            None,
            [['med'], [4.95]]
        ),
        
        (
            None,
            "count=max", #Столбца не существует 
            None,
            None
        ),
        
        (
            None,
            "rating avg", #Неправильно прописан аргумент
            None,
            None
        ),
        
        (
            "brand=xiaomi", 
            None,
            None,
            [['name', 'brand', 'price', 'rating'], 
            ['redmi note 12', 'xiaomi', '199', '4.6'], 
            ['poco x5 pro', 'xiaomi', '299', '4.4'], 
            ['redmi 10c', 'xiaomi', '149', '4.1']]
        ),
        #ДАННЫЕ ДЛЯ ТЕСТИРОВАНИЯ АГРЕГАЦИИ КОНЕЦ
    ]
)
def test_logic_handler(where_arg, order_by_arg, aggregate_arg, expected_result):
    
    test_data = [
        ['name', 'brand', 'price', 'rating'],
        ['iphone', 'apple', '999', '4.9'],
        ['iphone 16 pro max', 'apple', '1299', '5'],
        ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
        ['redmi note 12', 'xiaomi', '199', '4.6'],
        ['galaxy a54', 'samsung', '349', '4.2'],
        ['poco x5 pro', 'xiaomi', '299', '4.4'],
        ['galaxy z flip 5', 'samsung', '999', '4.6'],
        ['redmi 10c', 'xiaomi', '149', '4.1'],
    ]
    
    fake_args = argparse.Namespace(
        where=where_arg, 
        order_by=order_by_arg,
        aggregate=aggregate_arg
    )
    
    actual_result = proccess_data(test_data, fake_args)
    
    assert actual_result == expected_result