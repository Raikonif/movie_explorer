import re
from reader import get_list_of_dictionaries
# a function that returns True if letter is vowel
fe = '2022 monday 07 16:45'

def filter_movies_by_rating(rating_input):
    list_ratings = get_list_of_dictionaries("ratings")
    list_ratings_filtered = filter(lambda dictionary: (dictionary["rating"] == rating_input), list_ratings)
    new_list = []
    for element in list_ratings_filtered:
      new_list.append(element["movieId"])

    return list(set(new_list))


def get_movies_by_rating(rating):
    new_list = []
    list_ids_movies = filter_movies_by_rating(rating)
    list_movies = get_list_of_dictionaries("movies")
    for element in list_movies:
      new_dic = {}
      if element["movieId"] in list_ids_movies:
        new_dic["title"] = element["title"]
        numbers_date = re.findall('[0-9]+', element["title"])
        for number in numbers_date:
          if int(number)>1000:
            date_re = number
        new_dic["date_release"] = date_re 
        new_dic["genres"] = element["genres"]
        new_dic["rating"] = [rating,fe]
        new_list.append(new_dic)

    return new_list