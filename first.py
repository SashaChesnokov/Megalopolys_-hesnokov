from base_functions import read_csv, save_to_csv

def get_streams(song):
    '''
    Функция для высичления средней оценки учеников.
 
    Args:
        song (list): Песня, для которой нужно вычислить кол-во прослушиваний.
    Returns:
        correct_streams (int): Кол-во прослушиваний.
    '''
    date = list(map(int, song[3].split('.')))
    date_difference = abs((date[2]*365 + date[1]*30 + date[0])-(2023*365 + 5*30 + 12))
    correct_streams = int(abs((date_difference)/(len(song[1])+len(song[2])))*10000)
    return correct_streams

def correct_songs_data(songs_data):
    '''
    Функция для исправления кол-ва прослушиваний.
 
    Args:
        songs_data (list of lists): Список списков с данными о песнях.
    Returns:
        songs_data (list of lists): Список списков с данными о песнях.
    '''
    for song in songs_data:
        if song[0] == '0':
            song[0] = str(get_streams(song))
    return songs_data

def find_song(songs_data):
    '''
    Функция для поиска песен, которые вышли до определённой даты..
 
    Args:
        songs_data (list of lists): Список списков с данными о песнях.
    Returns:
        songs_data (list of dict): Список списков с данными о песнях.
    '''
    for song in songs_data[1:]:
        date = list(map(int, song[3].split('.')))
        if (date[0] == 1) and (date[1] == 1) and (date[2] == 2002):
            print(f"{song[2]} - {song[1]} - {song[0]}")
        elif (date[2] < 2002):
            print(f"{song[2]} - {song[1]} - {song[0]}")
def main():
    songs_data = read_csv('songs.csv')
    find_song(songs_data)
    songs_data = correct_songs_data(songs_data)
    save_to_csv(songs_data, "songs_new.csv")


main()
