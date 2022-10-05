import os
import sys
import csv
from pathlib import Path
from operator import itemgetter
import re


def search_files_csv(path):
    with os.scandir(Path(path)) as entries:
        files = [f.name for f in entries if f.name.endswith('movies.csv')]
    return files


def list_movies_desc_asc(path, input_user):
    # path = '../movie_files'
    files = search_files_csv(Path(path))
    list_of_dict_movies = []
    list_sorted = []
    # print(files)
    for file in files:
        # print(file)
        concat_dir = path + '/' + file
        if os.path.exists(concat_dir):
            # print(concat_dir)
            print('Please Wait...')
            with open(concat_dir, 'r', encoding='utf-8') as file_name:
                file_char_replaced = [line.replace(',', ' ') for line in file_name]
                reader = csv.reader(file_char_replaced, delimiter=',')
                for row in reader:
                    str_row = str(row)
                    first_replace = str_row.replace(' ', ',', 1).replace('[', '').replace("'", '').replace('"', '')
                    reversed_row = first_replace[::-1]
                    str_row = reversed_row.replace(' ', ',', 1).replace(']', '').replace("'", '').replace('"', '')
                    str_row = str_row[::-1]
                    row_formatted = str_row.strip().split(',')
                    dict_movie = {
                               'movieId': row_formatted[0],
                               'title': row_formatted[1],
                               'genres': row_formatted[2]
                            }
                    list_of_dict_movies.append(dict_movie)
                if input_user == 1:
                    list_of_dict_movies.sort(key=lambda m: m['title'])
                elif input_user == 2:
                    list_of_dict_movies.sort(key=lambda m: m['title'], reverse=True)

                list_print = [print(dict_movie) for dict_movie in list_of_dict_movies]
                return list_of_dict_movies


if __name__ == '__main__':
    # input_user = 'Toy Story'
    path = '../movie_files'
    list_movies_desc_asc(path, 1)
