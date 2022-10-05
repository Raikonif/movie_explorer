import os
import sys
import csv
from operator import itemgetter
import re


def search_files_csv(path):
    with os.scandir(path) as entries:
        files = [f.name for f in entries if f.name.endswith('movies.csv')]
    return files


def list_movies_desc_asc(path, input_user):
    # path = '../movie_files'
    files = search_files_csv(path)
    list_of_dict_movies = []
    list_sorted = []
    print(files)
    for file in files:
        # print(file)
        concat_dir = path + '/' + file
        if os.path.exists(concat_dir):
            print(concat_dir)
            with open(concat_dir, 'r', encoding='utf-8') as file_name:
                file_char_replaced = [line.replace(',', ' ') for line in file_name]
                reader = csv.reader(file_char_replaced, delimiter=',')
                for row in reader:
                    str_row = str(row)
                    first_replace = str_row.replace(' ', ',', 1).replace('[', '')
                    reversed_row = first_replace[::-1]
                    str_row = reversed_row.replace(' ', ',', 1).replace(']', '')
                    str_row = str_row[::-1]
                    row_formatted = str_row.strip().split(',')
                    dict_movie = {
                               'movieId': row_formatted[0],
                               'title': row_formatted[1],
                               'genres': row_formatted[2]
                            }
                    list_of_dict_movies.append(dict_movie)
                    list_of_dict_movies.sort(key=lambda m: m['title'])
                    # print(list_of_dict_movies.append(dict_movie))
                list_print = [print(dict) for dict in list_of_dict_movies]
                return list_print
                # for line in file_name.readlines()[1:]:
                #     line_formatted = line.strip().s(',')
                #     # line_formatted = line_formatted.remove(',')
                #     print(line_formatted)
                #     # if line_formatted[1].startswith('"') and line_formatted[1].endswith('"'):
                #     #     print(line_formatted)
                #
                # #     dict_movies = {
                # #         'movieId': line_formatted[0],
                # #         'title': line_formatted[1],
                # #         'genres': line_formatted[2]
                # #     }
                # #     list_of_dict_movies.append(dict_movies)
                # if input_user == 1:
                #     list_of_dict_movies.sort(key=lambda m: m['title'], reverse=True)
                # elif input_user == 2:
                #     list_of_dict_movies.sort(key=lambda m: m['title'], reverse=False)
                # #
                # list_print = [print(dict) for dict in list_of_dict_movies]
                # return list_of_dict_movies
                # if data is not None:
                #     pass
                # print(data)


if __name__ == '__main__':
    # input_user = 'Toy Story'
    path = '../movie_files'
    list_movies_desc_asc(path, 1)
