from reader import get_list_of_dictionaries
from datetime import datetime as dt
import re

def format_timestamp(data_ratings):
    for row in data_ratings: # "Monday, September 25, 2006 9:40:36 PM"
        row['timestamp'] = dt.strftime(dt.fromtimestamp(int(row['timestamp'])), '%A, %B %d, %Y %I:%M:%S %p')
    return data_ratings

def get_data_ratings(input_rating):
    data_ratings = get_list_of_dictionaries('ratings')
    data_ratings_filtered = [rating for rating in data_ratings if rating['rating'] == input_rating]
    data_ratings_filtered = format_timestamp(data_ratings_filtered)
    return data_ratings_filtered

def get_release_date(data_movies):
    for movie in data_movies:
        try:
            release_date = re.split(r'\((\d{4})\)', movie['title'])
            movie['title'] = release_date[0].rstrip()
            movie['release_date'] = release_date[1]
        except Exception as e:
            movie['release_date'] = 9999
    return data_movies


def get_data_movies(data_ratings):
    data_movies = get_list_of_dictionaries('movies')
    set_movie_id = set(movie['movieId'] for movie in data_ratings)
    data_movies_filtered = [movie for movie in data_movies if movie['movieId'] in set_movie_id]
    data_movies_filtered = get_release_date(data_movies_filtered)
    return data_movies_filtered

def generate_response(data_ratings, data_movies):
    for movie in data_movies:
        movie['ratings'] = [{'date_time' : rating['timestamp'],
                             'rating' : rating['rating']} for rating in
                            data_ratings if rating['movieId'] == movie['movieId']]
    return data_movies

def search_by_ratings(input_rating):
    data_ratings_filtered_by_inputed_rating = get_data_ratings(input_rating)
    data_movies_filtered_by_id = get_data_movies(data_ratings_filtered_by_inputed_rating)
    result = generate_response(data_ratings_filtered_by_inputed_rating, data_movies_filtered_by_id)
    return result



#if __name__ == '__main__':
#    search_by_ratings('3.0')
