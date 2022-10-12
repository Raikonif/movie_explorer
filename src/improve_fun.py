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
    line_formatted[2] = line_formatted[2].replace('|', ',').split(',')
    return line_formatted


def format_line_of_tags_ratings(line):
    line_formatted = line.strip().split(',')
    return line_formatted


def create_list_of_dicts_tag(list_line, list_of_dict_tag):
    dict_tag = {
        'userId': list_line[0],
        'movieId': list_line[1],
        'tag': list_line[2],
        'timestamp': list_line[3]
    }
    list_of_dict_tag.append(dict_tag)


def create_list_of_dicts_rating(list_line, list_of_dict_rating):
    dict_rating = {
        'userId': list_line[0],
        'movieId': list_line[1],
        'rating': list_line[2],
        'timestamp': list_line[3]
    }
    list_of_dict_rating.append(dict_rating)


def create_list_of_dict_movies(list_line, list_of_dict_movies):
    dict_movie = {
        'movieId': list_line[0],
        'title': list_line[1],
        'genres': list_line[2]
    }
    list_of_dict_movies.append(dict_movie)


def handle_open_file(concat_path, file, list_of_dict):
    with open(concat_path, 'r', encoding='utf-8') as file_name:
        if file == 'movies.csv':
            for line in file_name:
                list_line = format_line(line)
                create_list_of_dict_movies(list_line, list_of_dict)

        elif file == 'ratings.csv':
            for line in file_name:
                list_line = format_line_of_tags_ratings(line)
                create_list_of_dicts_rating(list_line, list_of_dict)

        elif file == 'tags.csv':
            for line in file_name:
                list_line = format_line_of_tags_ratings(line)
                create_list_of_dicts_tag(list_line, list_of_dict)

    return list_of_dict


# this fun use the functions above search_files_csv, format_line, create_list_of_dict_movies
def data_management(file):
    list_of_dict = []
    list_of_dict_movies = []
    list_of_dict_tag = []
    list_of_dict_rating = []
    concat_path = PATH + '/' + file
    if os.path.exists(concat_path) and file == 'movies.csv':
        list_of_dict = handle_open_file(concat_path, file, list_of_dict_movies)
        print(list_of_dict)

    elif os.path.exists(concat_path) and file == 'ratings.csv':
        list_of_dict = handle_open_file(concat_path, file, list_of_dict_rating)
        print(list_of_dict)

    elif os.path.exists(concat_path) and file == 'tags.csv':
        list_of_dict = handle_open_file(concat_path, file, list_of_dict_tag)
        print(list_of_dict)
    return list_of_dict


def convert_to_json_file(file):
    data = data_management(file)
    with open('movies.json', 'w+') as file:
        json.dump(data, file)
        print('json file created')


if __name__ == '__main__':
    input_user = 'Toy Story'
    # path = '../movie_files'
    # list_movies_desc_asc('desc')
    data_management('tags.csv')
    # convert_to_json_file('movies.csv')
