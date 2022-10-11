import os
import csv

from reader import get_list_of_dictionaries

PATH = '../movie_files'


def search_movie_title_typing(input_user):
    file= get_list_of_dictionaries("movies")
    list_dict = []
    exist = False
    for dict_movie in file:
        if input_user in dict_movie['title']:
            print(dict_movie)
            exist = True
            list_dict.append(dict_movie)
    if not exist:
        print('Movie not found')

    return list_dict


def search_movie_by_release_dates(title, release_date):
    file = get_list_of_dictionaries("movies")
    list_dict = []
    release_date = "({})".format(release_date)
    exist = False
    for dict_movie in file:
        if title == 'all' and release_date in dict_movie['title']:
            # print(dict_movie)
            list_dict.append(dict_movie)
            exist = True
        elif title != 'all' and release_date in dict_movie['title'] and title in dict_movie['title']:
            print(dict_movie)
            list_dict.append(dict_movie)
            exist = True

    if not exist:
        print('Movie not found')

    return list_dict


def list_movies_desc_asc(title, order, by):
    file = get_list_of_dictionaries("movies")
    # file = data_management()
    list_dict = []
    #file = data_management('movies.csv')
    if title == 'all' and order == 'desc' and by == 'title':
        print('DESC')
        file.sort(key=lambda m: m['title'])
    elif title == 'all' and order == 'asc' and by == 'title':
        print('ASC')
        file.sort(key=lambda m: m['title'], reverse=True)
    # for dict_movie in file:
    #     list_dict.append(dict_movie)
        # print(dict_movie)
        # print(dict_movie)
    return file
