import json
import os
import csv

PATH = '../movie_files'


def search_files_csv(path):
    with os.scandir(path) as entries:
        files = [f.name for f in entries if f.name.endswith('.csv')]
    return files


def format_line(line):
    replaced = line.replace(',', ' ')
    first_replace = replaced.replace(' ', ',', 1)
    reversed_row = first_replace[::-1]
    last_replace = reversed_row.replace(' ', ',', 1)
    row = last_replace[::-1]
    line_formatted = row.strip().split(',')
    line_formatted[2] = line_formatted[2].split('|')
    return line_formatted


def create_list_of_dict_movies(list_line, list_of_dict_movies):
    dict_movie = {
        'movieId': list_line[0],
        'title': list_line[1],
        'genres': list_line[2]
    }
    list_of_dict_movies.append(dict_movie)


# this fun use the functions above search_files_csv, format_line, create_list_of_dict_movies
def data_management():
    files = search_files_csv(PATH)
    print(files)
    list_of_dict_movies = []
    for file in files:
        concat_path = PATH + '/' + file
        if os.path.exists(concat_path):
            with open(concat_path, 'r', encoding='utf-8') as file_name:
                # reader = csv.reader(file_name, delimiter=',')
                for line in file_name:
                    list_line = format_line(line)
                    create_list_of_dict_movies(list_line, list_of_dict_movies)
            # list_print = [print(dict_movie) for dict_movie in list_of_dict_movies]
            # print(list_of_dict_movies)
            return list_of_dict_movies



def convert_to_json_file():
    data = data_management()
    with open('movies.json', 'w+') as file:
        json.dump(data, file)
        print('json file created')


if __name__ == '__main__':
    input_user = 'Toy Story'
    # path = '../movie_files'
    # list_movies_desc_asc('desc')
    data_management()
    # convert_to_json_file()
