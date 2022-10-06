from datetime import datetime as dt
import json, uuid

def save_responses(dict_file, unique_identifier):
    relative_path_save_responses = f'saved_responses/{unique_identifier}.json'
    with open(relative_path_save_responses, 'w', encoding='UTF-8') as file:
        json.dump(dict_file, file)


if __name__ == '__main__':
    dict_file = [
        {'key1' : 'value1'},
        {'key2' : ['lista2', 'lista3']},
        {'key3' : 100.0},
    ]
    unique_identifier = str(uuid.uuid4())
    save_responses(dict_file=dict_file, unique_identifier=unique_identifier)