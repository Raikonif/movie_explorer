import os
import csv

def count_titles_by_genre(asc = None):
    absolute_path = os.path.dirname(__file__)
    full_path = absolute_path.replace('src','movie_files')
    genres_Dict = {}
    count = 0
    genres = sort_by_genre()
    for element in genres:
        genres_Dict.update({element: count})
    print(type(genres_Dict))    
    files = search_files_csv(full_path)
    concat_dir = full_path + '/' + files    
    with open(concat_dir, 'r', encoding='utf-8') as movies_csv:
        csv_reader = csv. reader(movies_csv)
        rows = list(csv_reader)
        rows.pop(0)
        for row in rows :
            for genre in row[2].split('|'):
                if genre in genres_Dict:
                    genres_Dict[genre]+=1
    if  asc == 'asc':                
        sorted_dict_by_value = dict(sorted(genres_Dict.items(), key=lambda item: item[1]))                
        return sorted_dict_by_value
    elif asc == 'desc':
        sorted_dict_by_value = dict(sorted(genres_Dict.items(), key=lambda item: item[1],reverse = True))                
        return sorted_dict_by_value                     
    
    return genres_Dict


def search_files_csv(path):
    
    with os.scandir(path) as entries:
        files = [f.name for f in entries if f.name.endswith('movies.csv')]
        listToStr = ''.join([str(elem) for elem in files])
    return listToStr


def sort_by_genre():
    absolute_path = os.path.dirname(__file__)
    full_path = absolute_path.replace('src','movie_files')
    files = search_files_csv(full_path)
    concat_dir = full_path + '/' + files
    #print(path)
    #print( concat_dir)
    with open(concat_dir, 'r', encoding='utf-8') as movies_csv:
        filter_gen = list()
        csv_reader = csv. reader(movies_csv)
        #print(type(csv_reader))
        rows = list(csv_reader)
        rows.pop(0)
        for row in rows :
            for genre in row[2].split('|'):
                if not genre in filter_gen: # if dic has genre askey
                    filter_gen.append(genre) # dic en key +1
        #genres_list = list(set(filter_gen))
        #genres_list.sort()
        filter_gen.sort()   
    return filter_gen      
            
#print(search_files_csv('./movie_files'))
#print(type(search_files_csv('./movie_files')))
#print(sort_by_genre(full_path, 'Romance'))

if __name__ == '__main__':
    input_user = 'Toy Story'
    #path = './movie_files'
    #list_movies_desc_asc(path, 1)