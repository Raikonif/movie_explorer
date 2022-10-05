def get_tags():
  path = '../../movie_files/tags.csv'
  print("_________________")
  position = 1
  with open(path,"r") as file_tags:
    for line in file_tags:
      print(line)

get_tags()