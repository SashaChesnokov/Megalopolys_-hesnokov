import csv

def read_csv(file_path):
    '''
    Функция для считывания данных из csv файла.
 
    Args:
        file_path (str): Путь к файлу.
    Returns:
        student_data (list of dict): Список словарей с данными студентов.
    '''
    student_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            student_data.append(row[0].split(';'))
    
    return student_data

def save_to_csv(data, file_name):
    '''
    Запись данных в CSV формате в файл.
    
    Args:
    data (list of dict): Список словарей с данными студентов.
    file_name (str): Имя Файла для сохранения.
    '''
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter =';')
        # writer.writerow(['streams','artist_name','track_name','date'])
        writer.writerows(data)


def main():
    data = read_csv('tmp.csv')
    for i in data:
        print(i)
    # save_to_csv(data, 'tmp.csv')

main()