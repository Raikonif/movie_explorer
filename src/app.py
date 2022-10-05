import sys
from helpers.utility_help import get_argument

# if __name__ == '__main__':
get_argument(sys.argv[1])
    # result = search_files_csv('../movie_files')
    # print(result)
    # print('hello world!')
    

# def validate_comand(list_comands):
#   if list_comands[1] == "--help":
#     print("mostrar funcion principal")
#   else:
#     conver_dictionary(list_comands[1:])

# def conver_dictionary(list_values):
#   list_key = [key for key in list_values if '--' in key]
#   list_dict = [value for value in list_values if '--' not in value]
#   arguments_dic = dict(zip(list_key, list_dict))

#   return arguments_dic


