import csv
from base_functions import read_csv

def quicksort(songs_data, start, end):
    '''
    Функция для быстрой сортировки.
 
    Args:
        songs_data (list of lists): Список списков с данными о песнях.
    Returns:
        songs_data (list of lists): Список списков с данными о песнях.
    '''
    if end - start > 1:
        p = partition(songs_data, start, end)
        quicksort(songs_data, start, p)
        quicksort(songs_data, p + 1, end)
    return songs_data
 
 
def partition(songs_data, start, end):
    '''
    Функция использьзующая схему разбиения Хоара.

    Args:
        songs_data (list of lists): Список списков с данными о песнях.
    
    '''
    date = list(map(int, songs_data[start][3].split('.')))
    pivot = date[0] + date[1]*30 + date[2]*365
    i = start + 1
    j = end - 1
 
    while True and (i<len(songs_data)):
        date_i = list(map(int, songs_data[i][3].split('.')))
        s_i = date_i[0] + date_i[1]*30 + date_i[2]*365
        while (i <= j and s_i <= pivot):
            date_i = list(map(int, songs_data[i][3].split('.')))
            s_i = date_i[0] + date_i[1]*30 + date_i[2]*365
            i = i + 1
        
        date_j = list(map(int, songs_data[j][3].split('.')))
        s_j = date_j[0] + date_j[1]*30 + date_j[2]*365
        while (i <= j and s_j >= pivot):
            date_j = list(map(int, songs_data[j][3].split('.')))
            s_j = date_j[0] + date_j[1]*30 + date_j[2]*365
            j = j - 1
 
        if i <= j:
            songs_data[i], songs_data[j] = songs_data[j], songs_data[i]
        else:
            songs_data[start], songs_data[j] = songs_data[j], songs_data[start]
            return j


def print_top(songs_data, count):
    '''
    Функция для вывода ранних песен.
 
    Args:
        songs_data (list of lists): Список списков с данными о песнях.
        count (int): Количество песен, информацию о которых нужно вывести.
    '''

    place = 1
    for song in songs_data[:count]:
        print(f"{place} {song[2]}, {song[1]}, {song[3]}")
        place += 1


def main():
    songs_data = read_csv('songs_new.csv')
    songs_data = quicksort(songs_data[1:], 0, len(songs_data[1:]))
    print_top(songs_data, 5)
    
 
main()