from core_functions import data_management
import os
import csv

def count_titles_by_genre(asc = None):
    genres_Dict = {}
    count = 0
    movies_list = data_management()
    movies_list.pop(0)
    genres = sort_by_genre()
    for element in genres:
        genres_Dict.update({element: count})
    for row in movies_list :
        for genre in row['genres']:
            if genre in genres_Dict:
                genres_Dict[genre]+=1   
    if  asc == 'asc':                
        sorted_dict_by_value = dict(sorted(genres_Dict.items(), key=lambda item: item[1]))                
        return sorted_dict_by_value
    elif asc == 'desc':
        sorted_dict_by_value = dict(sorted(genres_Dict.items(), key=lambda item: item[1],reverse = True))                
        return sorted_dict_by_value                     
    return genres_Dict


def sort_by_genre():
    filter_gen = list()
    movies_list = data_management()
    movies_list.pop(0)
    for movie in movies_list :
        #print(movie)
        for genre in movie['genres']:
            if not genre in filter_gen and genre[0].isupper(): 
                filter_gen.append(genre) 
    genres_list = list(set(filter_gen))
    genres_list.sort()
    filter_gen.sort()
      
    return filter_gen 
            