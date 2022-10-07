from core_functions import data_management
import uuid
from save_responses import save_responses

def get_genres():
    filter_gen = list()
    movies_list = data_management()
    movies_list.pop(0)
    for movie in movies_list :
        for genre in movie['genres']:
            if not genre in filter_gen and genre[0].isupper(): 
                filter_gen.append(genre) 
    genres_list = list(set(filter_gen))
    genres_list.sort()
    filter_gen.sort()
    return filter_gen 



def create_obj(data):
    response_dic = {}
    response_dic['request_id'] = str(uuid.uuid4())
    response_dic['data'] = data
    response_dic['size'] = len(data) 
    save_responses(response_dic,response_dic['request_id']) 


def count_titles_by_genre(asc = None):
    genres_Dict = {}
    count = 0
    movies_list = data_management()
    movies_list.pop(0)
    genres = get_genres()
    for element in genres:
        genres_Dict.update({element: count})
    for row in movies_list :
        for genre in row['genres']:
            if genre in genres_Dict:
                genres_Dict[genre]+=1   
    if  asc == 'asc':                
        genres_Dict = dict(sorted(genres_Dict.items(), key=lambda item: item[1]))                   
    elif asc == 'desc':
        genres_Dict = dict(sorted(genres_Dict.items(), key=lambda item: item[1],reverse = True))                
    create_obj(genres_Dict)                       
    return genres_Dict


def sort_by_genre():
    filter_gen = get_genres()
    create_obj(filter_gen)
    return filter_gen 
            