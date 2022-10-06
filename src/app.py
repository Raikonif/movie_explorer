from helpers.constants import MAIN_DICTIONARY
from helpers.utility_help import validate_comand
import argparse


# def is_order_and_by_in_dictionary(dictionary):
#     return True if dictionary.get('order') != None and dictionary.get('by') != None else False

# def is_release_date_in_dictionary(dictionary):
#     return True if dictionary.get('release_date') != None else False

# def is_tag_in_dictionary(dictionary):
#     return True if dictionary.get('tag') != None else False

# def is_order_and_by_in(dictionary):
#     return True if dictionary.get('order') != None and dictionary.get('by') != None else False


# def is_release_date_in(dictionary):
#     return True if dictionary.get('release_date') != None else False


# def is_tag_in(dictionary):
#     return True if dictionary.get('tag') != None else False


# def validate_comand(dictionary):
#   if dictionary.get('title') == None and dictionary.get('genres') == None and dictionary.get('rating') == None:
#     print("Introduce --help to know comands available")
#   else:
#       if dictionary.get('title') != None:
#           if is_order_and_by_in(dictionary):
#               # Call function to get movies data ordered [desc,ascd] by ['title','tag','genre','rating']
#               list_movies_desc_asc(dictionary['title'], dictionary['order'], dictionary['by'])
#           elif is_release_date_in(dictionary):
#               # Call function to get movies that have the especified date release
#               search_movie_by_release_dates(dictionary['title'], dictionary['release_date'])
#           elif dictionary.get('order') != None or dictionary.get('by') != None:
#               # option ORDER and BY work together, the user must introduce both
#               print("Introduce --help to know comands available, ORDER and BY options works together")
#           else:
#               # The only option introduced was title, we call function that returns all movies.
#               search_movie_title_typing(dictionary['title'])
#       elif dictionary.get('genres') != None:
#           # The only option introduced was --GENRE, we call a function that return movies that belong to the same genre.
#           pass
#       elif dictionary.get('rating') != None:
#           # The only option introduced was --RATING, we call a function that return movies that have the same rate
#           pass
#       else:
#           print("Introduce --help to know comands available")



def manage_user_input():
  parser = argparse.ArgumentParser("Line Comands Available")

  parser.add_argument('-t', '--title', type=str, help=MAIN_DICTIONARY["--title"])
  parser.add_argument('-g', '--genres', type=str, help=MAIN_DICTIONARY["--genres"])
  parser.add_argument('-r', '--rating', type=str, help=MAIN_DICTIONARY["--rating"])
  parser.add_argument('-l', '--tag', type=str, help=MAIN_DICTIONARY["--tag"])
  parser.add_argument('-d', '--release_date', type=str, help=MAIN_DICTIONARY["--release_date"])
  parser.add_argument('-o', '--order', type=str, help=MAIN_DICTIONARY["--order"])
  parser.add_argument('-b', '--by', type=str, help=MAIN_DICTIONARY["--by"])

  args = parser.parse_args()
  dict_options_args = vars(args)

  validate_comand(dict_options_args)





manage_user_input()























# def iniciar():
# =======



#   parser = argparse.ArgumentParser("this a description")

#   parser.add_argument('-t', '--title', type=str, metavar='N', help=MAIN_DICTIONARY["--title"][0])
#   parser.add_argument('-g', '--genres', type=str, help=MAIN_DICTIONARY["--genres"][0])
#   parser.add_argument('-r', '--rating', type=str, help=MAIN_DICTIONARY["--rating"][0])
#   parser.add_argument('-l', '--tag',type=str, help=MAIN_DICTIONARY["--tag"][0])
#   parser.add_argument('-d', '--release_date', type=str, help=MAIN_DICTIONARY["--release_date"][0])
#   parser.add_argument('-o', '--order', type=str, help=MAIN_DICTIONARY["--order"][0])
#   parser.add_argument('-b', '--by', type=str, help=MAIN_DICTIONARY["--by"][0])



#   args = parser.parse_args()

#   variables = vars(args) 
#   print(variables)
#   #parser.add_argument('-t', '--tittle', type=str, help='nombre de la pelicula a buscar')
#   if variables.get('title') == None and variables.get('genres') == None and variables.get('rating') == None:
#     print("NO HACE NADA")
#   else:
#     if variables.get('title') != None:
#       if is_order_and_by_in_dictionary(variables):
#         print("ejecutamos serach sort movies by [title] order [desc]")
#       elif is_release_date_in_dictionary(variables):
#         print("llamamos a la funcion title  y le pasamos [release_date]")
#       elif variables.get('order') != None or variables.get('by') != None:
#         print("no se admite order o by")
#       else:
#         print("solo pelis")
#     elif variables.get('genres') != None:
#       print("Llamamos a la funcion que obtiene los generos")
#     elif variables.get('rating') != None:
#       print("Llamamos a la funcio que obtiene por rating")
#     else:
#       print("comandos incorrectos")


# iniciar()
# =======






# parser = argparse.ArgumentParser("Line Comands Available")

# parser.add_argument('-t', '--title', type=str, metavar='N', help=MAIN_DICTIONARY["--title"][0])
# parser.add_argument('-g', '--genres', type=str, help=MAIN_DICTIONARY["--genres"][0])
# parser.add_argument('-r', '--rating', type=str, help=MAIN_DICTIONARY["--rating"][0])
# parser.add_argument('-l', '--tag', type=str, help=MAIN_DICTIONARY["--tag"][0])
# parser.add_argument('-d', '--release_date', type=str, help=MAIN_DICTIONARY["--release_date"][0])
# parser.add_argument('-o', '--order', type=str, help=MAIN_DICTIONARY["--order"][0])
# parser.add_argument('-b', '--by', type=str, help=MAIN_DICTIONARY["--by"][0])

# args = parser.parse_args()

# dict_options_args = vars(args)

#print(variables)
# parser.add_argument('-t', '--tittle', type=str, help='nombre de la pelicula a buscar')
# if variables.get('title') == None and variables.get('genres') == None and variables.get('rating') == None:
#     print("NO HACE NADA")
# else:
#     if variables.get('title') != None:
#         if is_order_and_by_in(variables):
#             print("ejecutamos serach sort movies by [title] order [desc]")
#             list_movies_desc_asc(variables['title'], variables['order'], variables['by'])
#         elif is_release_date_in(variables):
#             print("llamamos a la funcion title  y le pasamos [release_date]")
#             search_movie_by_release_dates(variables['title'], variables['release_date'])
#         elif variables.get('order') != None or variables.get('by') != None:
#             print("no se admite order o by")
#         else:
#             print("solo pelis")
#             search_movie_title_typing(variables['title'])

#     elif variables.get('genres') != None:
#         print("Llamamos a la funcion que obtiene los generos")
#     elif variables.get('rating') != None:
#         print("Llamamos a la funcio que obtiene por rating")
#     else:
#         print("comandos incorrectos")




# validate_comand(dict_options_args)





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
