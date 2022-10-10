import json
import pprint


def save_responses(dict_file, unique_identifier):
    new_dic = {"ID": str(unique_identifier), "DATA": dict_file, "SIZE": len(dict_file)}
    pprint.pprint(new_dic)
    relative_path_save_responses = f'saved_responses/{unique_identifier}.json'
    with open(relative_path_save_responses, 'w', encoding='UTF-8') as file:
        json.dump(new_dic, file, indent=4)
