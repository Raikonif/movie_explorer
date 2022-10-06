import csv
import re
from pathlib import Path
from src.search_sort_movies import list_movies_desc_asc

absolute_path_ratings = 'C:/workspace/Jala/Python/dev_demos/final assignment/project/movie_explorer/movie_files/ratings.csv'
#relative_path_movies = 'C:/workspace/Jala/Python/dev_demos/final assignment/project/movie_explorer/movie_files/movies.csv'

#relative_path_rattings = '../ratings.csv'
relative_path_movies = '../../movie_files'


def get_ratings_data(input_rating=0.0):
    csv_data_ratings = []
    with open(Path(absolute_path_ratings), 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(file)
        csv_data_ratings = [row for row in reader if float(row[2]) >= input_rating]
    return csv_data_ratings


def get_release_date(movie):
    try:
        release_year = re.search(r"\((\d*)\)", movie).group(1)
        return release_year
    except:
        return 99999

def replace_title(movie_title):
    try:
        movie_title.replace(re.search(r"\((\d*)\)", movie).group(1))
        return movie_title
    except:
        return 99999


def get_movies_data(csv_data_ratings, input_rating):
    list_data_movies_filtered = []
    list_data_movies = list_movies_desc_asc(relative_path_movies, input_user=1)
    set_moveId = set([row[1] for row in csv_data_ratings])
    for move_id in set_moveId:
        list_data_movies_filtered.append([dict_obj for dict_obj in list_data_movies if dict_obj['movieId'] == move_id])
    for movie in list_data_movies_filtered:
        movie[0]['release_date'] = get_release_date(movie[0]['title'])
        movie[0]['title'] = replace_title(movie[0]['title'])
    return list_data_movies_filtered


def generate_response_search_ratings(list_ratings):
    for rating in list_ratings:
        pass


def search_by_ratings(input_rating):
    csv_data_ratings = []
    movies_data = []
    # if receives all -> return entire list of movies and ratings
    if type(input_rating) == float or type(input_rating) == int:
        csv_data_ratings = get_ratings_data(input_rating)
    if csv_data_ratings:
        movies_data = get_movies_data(csv_data_ratings, input_rating=input_rating)
    print(movies_data)



if __name__ == '__main__':
    # input_user = '3.0'
    path = '../movie_files'
    search_by_ratings(input_rating=4.0)
