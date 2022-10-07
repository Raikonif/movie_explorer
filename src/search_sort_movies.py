import os
import csv

from core_functions import data_management

PATH = '../movie_files'


def search_movie_title_typing(input_user):
    file = data_management()
    exist = False
    for dict_movie in file:
        if input_user in dict_movie['title']:
            print(dict_movie)
            exist = True
    if not exist:
        print('Movie not found')


def search_movie_by_release_dates(title, release_date):
    file = data_management()
    release_date = "({})".format(release_date)
    exist = False
    for dict_movie in file:
        if title == 'all' and release_date in dict_movie['title']:
            print(dict_movie)
            exist = True
        elif title != 'all' and release_date in dict_movie['title'] and title in dict_movie['title']:
            print(dict_movie)
            exist = True

    if not exist:
        print('Movie not found')


def list_movies_desc_asc(title, order, by):
    file = data_management()
    if title == 'all' and order == 'desc' and by == 'title':
        file.sort(key=lambda m: m['title'])
    elif title == 'all' and order == 'asc' and by == 'title':
        file.sort(key=lambda m: m['title'], reverse=True)
    for dict_movie in file:
        print(dict_movie)

#
# if __name__ == '__main__':
#     input_user = 'Toy Story'
#     # path = '../movie_files'
#     # list_movies_desc_asc('all', 'desc', 'title')
#     # search_movie_title_typing(input_user)
#     search_movie_by_release_dates('all', '1995')
