def get_tags():
  path = '../../movie_files/tags.csv'
  print("_________________")
  with open(path,"r") as file_tags:
    for line in file_tags:
      pass

#get_tags()

ejemplo = "2,60756,funny,1445714994"

def get_list_from_string(str_line):
  new_list = []
  new_list.append(str_line[0:str_line.find(",")])
  str_line = str_line[str_line.find(",")+1:]
  new_list.append(str_line[0:str_line.find(",")])
  str_line = str_line[str_line.find(",")+1:]
  size_of_last_element=len(str_line[::-1][0:str_line[::-1].find(",")][::-1])+1
  new_list.append(str_line[0:len(str_line)-size_of_last_element])
  new_list.append(str_line[::-1][0:str_line[::-1].find(",")][::-1])
  return new_list


def get_dictionary_from_list(list_data):
  pass