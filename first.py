from base_functions import read_csv, save_to_csv

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

main()
