import csv
from pathlib import Path
from src.search_sort_movies import list_movies_desc_asc

absolute_path_ratings = 'C:/workspace/Jala/Python/dev_demos/final assignment/project/movie_explorer/movie_files/ratings.csv'
#relative_path_movies = 'C:/workspace/Jala/Python/dev_demos/final assignment/project/movie_explorer/movie_files/movies.csv'

#relative_path_rattings = '../ratings.csv'
relative_path_movies = '../movie_files'

def get_ratings_data(input_rating=0.0):
    csv_data_ratings = []
    with open(Path(absolute_path_ratings), 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(file)
        csv_data_ratings = [row for row in reader if float(row[2]) >= input_rating]
    return csv_data_ratings


def get_movies_data(csv_data_ratings):
    list_data_movies = []
    list_data_movies_filtered = []
    set_moveId = set([row[1] for row in csv_data_ratings])  # len= = 8452
    list_data_movies = list_movies_desc_asc(relative_path_movies, input_user=1)
    list_data_movies_filtered = []


def generate_response_search_ratings(list_ratings):
    for rating in list_ratings:
        pass


def search_by_ratings(input_rating):
    csv_data_ratings = []
    data_movies = []
    if type(input_rating) == float or type(input_rating) == int:
        csv_data_ratings = get_ratings_data(input_rating)
    if csv_data_ratings:
        movies_data = get_movies_data(csv_data_ratings)


if __name__ == '__main__':
    # input_user = '3.0'
    path = '../movie_files'
    search_by_ratings(input_rating=3.0)
