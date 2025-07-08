import csv

def load_data_from_csv(path: str):
    data = []
    try:
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
            return data
    except FileNotFoundError:
        return None