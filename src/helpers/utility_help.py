import sys
from helpers.constants import MAIN_DICTIONARY


def get_argument(arg_key):
  is_argument = False
  for key, value in MAIN_DICTIONARY.items():
    if arg_key == key:
      is_argument = True
      value[1]()
      break

  if is_argument == False:
    print("not valid comand. Please try to write down app.py --help")



# def join_elements_list(list_comands):
#   listToStr = ' '.join([str(elem) for elem in list_comands])
#   return listToStr


def validate_input(arg_list):
  pass

