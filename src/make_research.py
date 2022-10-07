'''
 title, gender, rating, tag, release_date
 los problemas son tag y rating

 Regex: '.*'


'''
import re
def get_data():
    dict_data = [
        [{'moveId' : 1}, {'title' : 'title1 (1996)'}, {'genres' : 'Drama|Comedia|'},
         {'tags' : ['funny','tag2','tag3']}, {'release_date' : '1996'}, {'ratings' : [{'rating' : 'value rating 1'},
                    {'rating' : 'value ratings 2'}]}],

        [{'moveId': 2}, {'title': 'title2 (2006)'}, {'genres': 'Horror|Suspense'},
         {'tags': ['family', 'tag4', 'tag5']}, {'release_date' : '2006'}, {'ratings': [{'rating': 'value rating 3'},
                    {'rating': 'value ratings 4'}]}]
    ]
    return dict_data

def filter_data_with_input_args(data_csv, input_args):
    filtered_data = []
    #filtered_data = [item for item in data_csv if data_csv[0]['moveId'] == '.*'
    #                                                and data_csv[1]['title'] == '.*'
    #                                                and data_csv[2]['genres'] == '.*'
    #                                                and data_csv[3]['tags'] == '.*'
    #                                                and data_csv[4]['release_date'] == '.*'
    #                                                and data_csv[5]['ratings'] == '.*']
    filtered_data = [item for item in data_csv if re.match('title', str(data_csv[0]['moveId']))]
    return filtered_data

def research(input_args):
    data_csv = get_data()
    filtered_data = []
    for movie in data_csv:
        filtered_data.append(filter_data_with_input_args(data_csv=movie, input_args=input_args))
    print(filtered_data)





if __name__ == '__main__':
    research({'title': 'Toy Story', 'genres': '.*', 'rating': '.*', 'tag': '.*', 'release_date': '.*', 'order': '.*', 'by': '.*'})