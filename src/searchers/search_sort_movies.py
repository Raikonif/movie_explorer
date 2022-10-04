import os
import sys


def search_files_csv(path):
    with os.scandir(path) as entries:
        files = [f.name for f in entries if f.name.endswith('movies.csv')]
    return files


def list_movies_desc_asc(input_user):
    path = '../movie_files'
    files = search_files_csv(path)
    list_of_dict_movies = []
    list_temporary = []
    print(files)
    for file in files:
        # print(file)
        concat_dir = path + '/' + file
        if os.path.exists(concat_dir):
            print(concat_dir)
            with open(concat_dir, 'r', encoding='utf-8') as file_name:
                for line in file_name.readlines():
                    # data = file_name.readline()
                    # list_formatted = [line.strip() for line in data]
                    line_formatted = line.strip().split(',')
                    dict_movies = {'movieId': line_formatted[0], 'title': line_formatted[1],'genres': line_formatted[2]}
                    list_of_dict_movies.append(dict_movies)
                    # print(dict_movies)

                print(list_of_dict_movies)

                # if data is not None:
                #     pass
                    # print(data)


if __name__ == '__main__':
    input_user = 'Toy Story'
    list_movies_desc_asc(input_user)
