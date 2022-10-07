from itertools import count
from search_sort_movies import search_movie_title_typing, list_movies_desc_asc, search_movie_by_release_dates
from genres_funcions import sort_by_genre, count_titles_by_genre
from search_ratings import search_by_ratings



def is_order_and_by_in(dictionary):
    return True if dictionary.get('order') != None and dictionary.get('by') != None else False


def is_release_date_in(dictionary):
    return True if dictionary.get('release_date') != None else False


def is_tag_in(dictionary):
    return True if dictionary.get('tag') != None else False



def validate_comand(dictionary):
    if dictionary.get('title') == None and dictionary.get('genres') == None and dictionary.get('rating') == None:
        print("Introduce --help to know comands available")
    else:
        if dictionary.get('title') != None:
            if is_order_and_by_in(dictionary):
                # Call function to get movies data ordered [desc,ascd] by ['title','tag','genre','rating']
                list_movies_desc_asc(dictionary['title'], dictionary['order'], dictionary['by'])
            elif is_release_date_in(dictionary):
                # Call function to get movies that have the especified date release
                search_movie_by_release_dates(dictionary['title'], dictionary['release_date'])
            elif dictionary.get('order') != None or dictionary.get('by') != None:
                # option ORDER and BY work together, the user must introduce both
                print("Introduce --help to know comands available, ORDER and BY options works together")
            else:
                # The only option introduced was title, we call function that returns all movies.
                search_movie_title_typing(dictionary['title'])
        elif dictionary.get('genres') != None:
            # The only option introduced was --GENRE, we call a function that return movies that belong to the same genre.
            # pass
            if dictionary['count'] is True:
                print(count_titles_by_genre(dictionary['order']))
            else:
                print(sort_by_genre())
        elif dictionary.get('rating') != None:
            # The only option introduced was --RATING, we call a function that return movies that have the same rate
            search_by_ratings(dictionary['rating'])
        else:
            print("Introduce --help to know comands available")