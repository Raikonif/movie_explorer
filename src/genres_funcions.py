from core_functions import data_management


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


def dic_to_list(dictionary):
    lista = []
    for key, value in dictionary.items():
        newdic = {}
        newdic['genre'] = key
        newdic['count'] = value
        lista.append(newdic)
    return lista    


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
        return dic_to_list(genres_Dict)                 
    elif asc == 'desc':
        genres_Dict = dict(sorted(genres_Dict.items(), key=lambda item: item[1],reverse = True)) 
        return dic_to_list(genres_Dict)                                      
    return dic_to_list(genres_Dict)


def sort_by_genre():
    filter_gen = get_genres()
    return filter_gen 