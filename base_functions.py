import csv

def read_csv(file_path):
    '''
    Функция для считывания данных из csv файла.
 
    Args:
        file_path (str): Путь к файлу.
    Returns:
        data (list of lists): Список списков с данными о песнях.
    '''
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[0].split(';'))
    
    return data

def save_to_csv(data, file_name):
    '''
    Запись данных в CSV формате в файл.
    
    Args:
    data (list of lists): Список списков с данными о песнях.
    file_name (str): Имя Файла для сохранения.
    '''
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writerЫ(file, delimiter =';')
        writer.writerows(data)