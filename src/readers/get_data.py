# return a list of lists that contains the data from tha csv files
def get_tags(str_name_file):
    fichero = "ratings"
    path = f'../../movie_files/{str_name_file}.csv'
    new_list = []
    with open(path, "r", encoding='utf-8') as file_tags:
        for line in file_tags:
            if str_name_file == "movies":
                new_list.append(convert_str_3_args_to_list(line))
            else:
                new_list.append(convert_str_4_args_to_list(line))

    return get_dictionary_from_list(new_list)


# get_tags()

# tags_example = "2,60756,funny,1445714994"userId,movieId,tag,timestamp
# ratings_example ="1,1,4.0,964982703"userId,movieId,rating,timestamp
# movies_example ="2,Jumanji (1995),Adventure|Children|Fantasy"movieId,title,genres

def convert_str_4_args_to_list(str_line):
    new_list = []
    new_list.append(str_line[0:str_line.find(",")])
    str_line = str_line[str_line.find(",") + 1:]
    new_list.append(str_line[0:str_line.find(",")])
    str_line = str_line[str_line.find(",") + 1:]
    size_of_last_element = len(str_line[::-1][0:str_line[::-1].find(",")][::-1]) + 1
    new_list.append(str_line[0:len(str_line) - size_of_last_element])
    new_list.append(str_line[::-1][0:str_line[::-1].find(",")][::-1][:-1])
    return new_list


def convert_str_3_args_to_list(str_line):
    new_list = []
    new_list.append(str_line[0:str_line.find(",")])
    str_line = str_line[str_line.find(",") + 1:]
    size_of_last_element = len(str_line[::-1][0:str_line[::-1].find(",")][::-1]) + 1
    new_list.append(str_line[0:len(str_line) - size_of_last_element])
    list_movies = str_line[::-1][0:str_line[::-1].find(",")][::-1][:-1]
    new_list.append(str_line[::-1][0:str_line[::-1].find(",")][::-1][:-1])
    return new_list


def get_dictionary_from_list(lists_of_data):
    new_list = []
    ignored_pos = 1

    for element in lists_of_data:
        new_dict = {}
        if ignored_pos == 1:
            ignored_pos += 1
        else:
            for position in range(len(element)):
                new_dict[lists_of_data[0][position]] = element[position]
            # new_dict[lists_of_data[0][0]]=element[0]
            # new_dict[lists_of_data[0][1]]=element[1]
            # new_dict[lists_of_data[0][2]]=element[2]
            # new_dict[lists_of_data[0][3]]=element[3]
            new_list.append(new_dict)

    return new_list


print((get_tags("movies")))
