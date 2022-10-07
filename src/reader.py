# return a list of lists that contains the data from tha csv files
import os


def get_list_of_dictionaries(str_name_file):
    path = f'../movie_files/{str_name_file}.csv'
    new_list = []
    if os.path.exists(path):
        with open(path, "r", encoding='utf-8') as file_data:
            for line in file_data:
                if str_name_file == "movies":
                    new_list.append(format_list_movies(line))
                else:
                    new_list.append(format_list_tags_ratings(line))

    return generate_list_of_dictionaries(new_list)


# get list of tags ans ratings
def format_list_tags_ratings(str_line):
    new_list = []
    new_list.append(str_line[0:str_line.find(",")])
    str_line = str_line[str_line.find(",") + 1:]
    new_list.append(str_line[0:str_line.find(",")])
    str_line = str_line[str_line.find(",") + 1:]
    size_of_last_element = len(str_line[::-1][0:str_line[::-1].find(",")][::-1]) + 1
    new_list.append(str_line[0:len(str_line) - size_of_last_element])
    new_list.append(str_line[::-1][0:str_line[::-1].find(",")][::-1][:-1])

    return new_list


# cambiar para get_list_movies_data(str_line)
def format_list_movies(str_line):
    new_list = []
    new_list.append(str_line[0:str_line.find(",")])
    str_line = str_line[str_line.find(",") + 1:]
    size_of_last_element = len(str_line[::-1][0:str_line[::-1].find(",")][::-1]) + 1
    new_list.append(str_line[0:len(str_line) - size_of_last_element])
    list_movies = str_line[::-1][0:str_line[::-1].find(",")][::-1][:-1]
    new_list.append(list_movies.split("|")) if list_movies != "genres" else new_list.append(list_movies)

    return new_list


def generate_list_of_dictionaries(lists_of_data):
    list_dictionaries = []
    ignored_pos = 1

    for element in lists_of_data:
        new_dict = {}
        if ignored_pos == 1:
            ignored_pos += 1
        else:
            for position in range(len(element)):
                new_dict[lists_of_data[0][position]] = element[position]
            list_dictionaries.append(new_dict)

    return list_dictionaries
