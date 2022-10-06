from datetime import datetime as dt
import json, uuid

def save_responses(dict_file, unique_identifier):
    relative_path_save_responses = f'saved_responses/{unique_identifier}.json'
    with open(relative_path_save_responses, 'w', encoding='UTF-8') as file:
        json.dump(dict_file, file)
