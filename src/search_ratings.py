import os, csv, re
from datetime import datetime as dt
import uuid
from core_functions import data_management
from save_responses import save_responses

relative_path_ratings = '../movie_files/ratings.csv'
relative_path_movies = '../movie_files/movies.csv'


def get_release_date(movie):
    try:
        release_year = re.search(r"\((\d*)\)", movie).group(1)
        return release_year
    except:
        return 99999


def data_ratings(input_rating):
    if os.path.exists(relative_path_ratings):
        with open(relative_path_ratings, 'r', encoding='utf-8') as file_name:
            reader = csv.reader(file_name, delimiter=',')
            next(reader)
            csv_data_ratings = [row for row in reader if float(row[2]) >= input_rating]
    return csv_data_ratings


def get_movies_data(csv_data_ratings, input_rating):
    list_data_movies_filtered = []
    list_data_movies = data_management()
    set_moveId = set([row[1] for row in csv_data_ratings])
    # for move_id in set_moveId:
    list_data_movies_filtered.append([dict_obj for dict_obj in list_data_movies if dict_obj['movieId'] in set_moveId])
    for movie in list_data_movies_filtered:
        movie[0]['release_date'] = get_release_date(movie[0]['title'])
    return list_data_movies_filtered


def get_data_formated(csv_data):
    format_date = '%A, %B %d, %Y, %I:%M:%S %p'
    for row in csv_data:
        row[-1] = dt.fromtimestamp(int(row[-1]))
        row[-1] = dt.strftime(row[-1], format_date)
    return csv_data


def get_ratings_data(input_rating=0.0):
    csv_data = []
    with open(relative_path_ratings, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(file)
        csv_data = [row for row in reader if float(row[2]) >= input_rating]
    csv_data = get_data_formated(csv_data)
    return csv_data


def generate_response_search_ratings(movies_data, csv_data_ratings):
    list_movies_with_ratings = []
    format_date = '%A, %B %d, %Y, %I:%M:%S %p'
    for movie in movies_data:
        movie[0]['ratings'] = [dict({'date_time': str(dt.strptime(rating[-1], format_date)),
                                     'rating': float(rating[2])}) for rating in csv_data_ratings if
                               movie[0]['movieId'] == rating[1]]
    print(movies_data)
    return movies_data


def search_by_ratings(variables):
    rating = float(variables)

    csv_data_ratings = []
    movies_data = []
    csv_data_ratings = get_ratings_data()
    if csv_data_ratings:
        movies_data = get_movies_data(csv_data_ratings, input_rating=rating)
    response_data = generate_response_search_ratings(movies_data=movies_data, csv_data_ratings=csv_data_ratings)
    id = unique_identifier = uuid.uuid4()
    print(response_data)
    save_responses(response_data, id)
