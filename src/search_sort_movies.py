import os
import csv

PATH = '../movie_files'


def search_files_csv(path):
    with os.scandir(path) as entries:
        files = [f.name for f in entries if f.name.endswith('movies.csv')]
    return files


# def search_and_open_file_if_exist(files):
#     for file in files:
#         concat_dir = path + '/' + file
#         if os.path.exists(concat_dir):
#             with open(concat_dir, 'r', encoding='utf-8') as file_name:
#                 reader = csv.reader(file_name)
#         return reader


def search_movie_title_typing(input_user):
    path = "../movie_files"
    files = search_files_csv(path)
    # reader = search_and_open_file_if_exist(files)
    for file in files:
        concat_dir = path + '/' + file
        if os.path.exists(concat_dir):
            with open(concat_dir, 'r', encoding='utf-8') as file_name:
                reader = csv.reader(file_name)
                exist = False
                for row in reader:
                    if input_user in row[1]:
                        print(row)
                        exist = True

                if not exist:
                    print('Movie not found')
                return row


def search_movie_by_release_dates(input_user):
    path = "../movie_files"
    files = search_files_csv(path)
    for file in files:
        concat_dir = path + '/' + file
        if os.path.exists(concat_dir):
            with open(concat_dir, 'r', encoding='utf-8') as file_name:
                reader = csv.reader(file_name)
                exist = False
                input_formatted = "({})".format(input_user)
                for row in reader:
                    if input_formatted in row[1]:
                        print(row)
                        exist = True

                if not exist:
                    print('Movie with that release not found')
                return row


# def data_management():
#     files = search_files_csv(PATH)
#     list_of_dict_movies = []
#     for file in files:
#         concat_path = PATH + '/' + file
#         if os.path.exists(concat_path):
#             with open(concat_path, 'r', encoding='utf-8') as file_name:
#                 for line in file_name:
#                     list_line = format_line(line)
#                     create_list_of_dict_movies(list_line, list_of_dict_movies)
#             list_print = [print(dict_movie) for dict_movie in list_of_dict_movies]
#             # print(list_of_dict_movies)
#             return list_of_dict_movies
#
#
# def format_line(line):
#     replaced = line.replace(',', ' ')
#     first_replace = replaced.replace(' ', ',', 1)
#     reversed_row = first_replace[::-1]
#     last_replace = reversed_row.replace(' ', ',', 1)
#     row = last_replace[::-1]
#     line_formatted = row.strip().split(',')
#     line_formatted[2] = line_formatted[2].replace('|', ',').split(',')
#     return line_formatted
#
#
# def create_list_of_dict_movies(list_line, list_of_dict_movies):
#     dict_movie = {
#         'movieId': list_line[0],
#         'title': list_line[1],
#         'genres': list_line[2]
#     }
#     list_of_dict_movies.append(dict_movie)
# def file_management(concat_path):
#     # print('concat_path', concat_path)
#     with open(concat_path, 'r', encoding='utf-8') as file_name:
#         for line in file_name:
#             format_file(line)


def list_movies_desc_asc(input_user):
    path = '../movie_files'
    files = search_files_csv(path)
    list_of_dict_movies = []
    for file in files:
        concat_dir = path + '/' + file
        if os.path.exists(concat_dir):
            print('Please Wait...')
            with open(concat_dir, 'r', encoding='utf-8') as file_name:
                file_char_replaced = [line.replace(',', ' ') for line in file_name]
                # print(file_char_replaced)
                reader = csv.reader(file_char_replaced, delimiter=',')
                for row in reader:
                    print(row)
                    str_row = str(row)
                    first_replace = str_row.replace(' ', ',', 1).replace('[', '').replace("'", '').replace('"', '')
                    reversed_row = first_replace[::-1]
                    str_row = reversed_row.replace(' ', ',', 1).replace(']', '').replace("'", '').replace('"', '')
                    str_row = str_row[::-1]
                    row_formatted = str_row.strip().split(',')
                    row_formatted[2] = row_formatted[2].replace('|', ',').split(',')
                    # print(row_formatted[2])
                    dict_movie = {
                        'movieId': row_formatted[0],
                        'title': row_formatted[1],
                        'genres': row_formatted[2]
                    }
                    list_of_dict_movies.append(dict_movie)
                if input_user == 'asc':
                    list_of_dict_movies.sort(key=lambda m: m['title'])
                elif input_user == 'desc':
                    list_of_dict_movies.sort(key=lambda m: m['title'], reverse=True)

                # list_print = [print(dict_movie) for dict_movie in list_of_dict_movies]
                return list_of_dict_movies


if __name__ == '__main__':
    input_user = 'Toy Story'
    # path = '../movie_files'
    # list_movies_desc_asc('desc')
    # data_management()
    # search_movie_title_typing(input_user)
    # search_movie_by_release_dates('1995')
