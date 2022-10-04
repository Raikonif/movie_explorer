def main_help():
  print()
  for key, element in MAIN_DICTIONARY.items():
    print(key + ":" , element[0], sep="\n")
    print()


def main_title():
  print("calling main_title function")


def main_ratin():
  print("calling main_ratin function")


def main_genres():
  print("calling main_genres function")


def main_tag():
  print("calling main_tag function")


# constant that content the comands available for the user
MAIN_DICTIONARY={
  "--help" :
  ["This comand show the all information of the data",main_help],

  "--title" :
  ['this function returns a list of movies. Insert "all" to return all the database, or specify the name of the wantde movie. Regex available. You can use it with "--sort" "by"',main_title],

  "--tag" : 
  ["This return something that I dont understand TODO",main_tag],

  "--rating" : 
  ["This comand show all movies that have the specified rating",main_ratin],

  "--genres" : 
  ["This will return a response that have movies that have the same genre",main_genres],

}

# python3 movies_explorer --help
# python3 movies_explorer --title all --order desc --by title
# python3 movies_explorer --title "doctorextrange"
# python3 movies_explorer --title Sabrina --release_date all
# python3 movies_explorer --title "Home Alone 2" --tag sequel
# python3 movies_explorer --rating 3.0
# python3 movies_explorer --genres [word]



# comands

# --help

# --title all
# --title "T" (any words)

# --order desc asc

# --by title count

# --title "T" (any words)

# --genre all or "Animation" (Any word)

# --release_date all or (any number)

# --tag "sequel" (any word)

# --ratings all or 3.0 (any float)

# --user 1 (any id)
