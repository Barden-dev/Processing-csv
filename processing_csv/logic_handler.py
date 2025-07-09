import argparse
import operator

OPERATOR_MAP = {
    '>': operator.gt,
    '<': operator.lt,
    '=': operator.eq,
}

def _apply_filter(data: list, column_index: int, value: str, operator: str):
    comparison_func = OPERATOR_MAP[operator]
    filtered_data = []

    for row in data:
        cell_value_str = row[column_index]
        try:
            numeric_cell = float(cell_value_str)
            numeric_target = float(value)
            if comparison_func(numeric_cell, numeric_target):
                filtered_data.append(row)
        except ValueError:
            if operator == '=' and cell_value_str == value:
                filtered_data.append(row)
    return filtered_data
    
    
def _apply_sort(data: list, column_index: int, operation: str):
    def get_key(row):
        value = row[column_index]
        try:
            return float(value)
        except ValueError:
            return value
        
    reverse_order = operation == 'desc'
    return sorted(data, key=get_key, reverse=reverse_order)
    
def _apply_aggregation(data: list, column_index: int, operation: str):
    column_values = [float(row[column_index]) for row in data if row[column_index]]

    match operation:
        case 'avg':
            value = sum(column_values) / len(column_values)
        case 'max':
            value = max(column_values)
        case 'min':
            value = min(column_values)
        case 'med':
            if len(column_values) % 2 != 0:
                value = sorted(column_values)[len(column_values) // 2]
            else:
                value = (sorted(column_values)[len(column_values) // 2] + sorted(column_values)[len(column_values) // 2 - 1]) / 2
    return [[operation], [value]]


def proccess_data(data: list, args: argparse.Namespace):
    header = data[0]
    data_rows = data[1:]
    
    #РАБОТА С ФИЛЬТРОМ
    if args.where:
        try:
            operator = [operator for operator in args.where if operator in OPERATOR_MAP]
            if len(operator) == 1:
                column, value = args.where.split(operator[0])
                if column in header:
                    data_rows = _apply_filter(data_rows, header.index(column), value, operator[0])
                else:
                    print("Ошибка, такого столбца не существует")
                    return
            else:
                raise
        except:
            print("Неверный формат аргумента, пример использования: -w \"brand=apple\" или -w \"rating>4.7\"")
            return
        

    #РАБОТА С СОРТИРОВКОЙ
    if args.order_by and '=' in args.order_by:
        column, operation = args.order_by.split('=')
        if column in header:
            data_rows = _apply_sort(data_rows, header.index(column), operation)
        else:
            print(f"Ошибка: столбец '{column}' для сортировки не найден.")
            return
    elif args.order_by:
        print("Неверный формат аргумента сортировки. Пример: --order-by \"price=desc\"")
        return


    #РАБОТА С АГРЕГАЦИЕЙ
    aggregation_result = None
    if args.aggregate and '=' in args.aggregate:
        column, operation = args.aggregate.split('=')
        if column in header:
            column_index = header.index(column)
            aggregation_result = _apply_aggregation(data_rows, column_index, operation)
        else:
            print("Ошибка, такого столбца не существует")
            return
    elif args.aggregate:
        print("Неверный формат аргумента, пример использования: -a \"rating=avg\"")
        return
    
    
    if aggregation_result:
        return aggregation_result
    else:
        return [header] + data_rows

