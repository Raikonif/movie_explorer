#import sys
from helpers.utility_help import get_argument
from helpers.constants import MAIN_DICTIONARY
import argparse
# if __name__ == '__main__':
#get_argument(sys.argv[1])
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

#print(MAIN_DICTIONARY["--help"][0])
def is_order_and_by_in_dictionary(dictionary):
  return True if dictionary.get('order') != None and dictionary.get('by') != None else False
#  return_if_true if condition else condition_if_false


#   if dictionary.get('order') == None and dictionary.get('by') == None:
#     return False
#   else:
#     return True

# 'Yes' if fruit == 'Apple' else 'No'



def is_release_date_in_dictionary(dictionary):
   return True if dictionary.get('release_date') != None else False

def is_tag_in_dictionary(dictionary):
   return True if dictionary.get('tag') != None else False






parser = argparse.ArgumentParser("this a description")

parser.add_argument('-t', '--title', type=str, metavar='N', help=MAIN_DICTIONARY["--title"][0])
parser.add_argument('-g', '--genres', type=str, help=MAIN_DICTIONARY["--genres"][0])
parser.add_argument('-r', '--rating', type=str, help=MAIN_DICTIONARY["--rating"][0])
parser.add_argument('-l', '--tag',type=str, help=MAIN_DICTIONARY["--tag"][0])
parser.add_argument('-d', '--release_date', type=str, help=MAIN_DICTIONARY["--release_date"][0])
parser.add_argument('-o', '--order', type=str, help=MAIN_DICTIONARY["--order"][0])
parser.add_argument('-b', '--by', type=str, help=MAIN_DICTIONARY["--by"][0])


args = parser.parse_args()

variables = vars(args) 
print(variables)
#parser.add_argument('-t', '--tittle', type=str, help='nombre de la pelicula a buscar')
if variables.get('title') == None and variables.get('genres') == None and variables.get('rating') == None:
  print("NO HACE NADA")
else:
  if variables.get('title') != None:
    if is_order_and_by_in_dictionary(variables):
      print("ejecutamos serach sort movies by [title] order [desc]")
    elif is_release_date_in_dictionary(variables):
      print("llamamos a la funcion title  y le pasamos [release_date]")
    elif variables.get('order') != None or variables.get('by') != None:
      print("no se admite order o by")
    else:
      print("solo pelis")
  elif variables.get('genres') != None:
    print("Llamamos a la funcion que obtiene los generos")
  elif variables.get('rating') != None:
    print("Llamamos a la funcio que obtiene por rating")
  else:
    print("comandos incorrectos")




# if --title Sabrina --release_date all == --title Sabrina --release_date all

# elif --title "Home Alone 2" --tag sequel

# elif --genres [word]

# else:
#   comando no valido

# python3 movies_explorer --help
# python3 movies_explorer --title all --order desc --by [title a - z] [ genres a - z] [ rating a-z ...]
# python3 movies_explorer --title "doctorextrange"
# python3 movies_explorer --title Sabrina --release_date all
# python3 movies_explorer --title "Home Alone 2" --tag sequel
# python3 movies_explorer --rating 3.0
# python3 movies_explorer --genres [word]

# --title                   => default = 'all'
#     --order               => default = 'desc'
#     --by                  => default = 'title'
#     --release_date        => default = 'all'     -> string date
#     --tag                 => default = 'all'





# --rating                  => default = 'all'
#     --order
#     --by
#     --release_date
#     --tag




# --genres                  => default = 'all'
#     --order
#     --by
#     --release_date
#     --tag



