MAIN_DICTIONARY={
  "--title" :
  'this function returns a list of movies. Introduce "all" to get all movies or "key_name" to get movies that have the word in the title movie. Introduce order[desc] or order[asc], and by[title] or by[genre] or by[rating] or by[tag] to get the list of movies ordered[mode] by[column_data]',

  "--genres" : 
  "This will return a list of movies of a specified genre --genres[genre_key_word]",

  "--rating" : 
  "This will return a list of movies of a specified rate --rating[rate_key_number]",

  "--tag" : 
  "This will return a list of movies of a specified tag --tag[tag_key_word]. This option works with --title",

  "--release_date" : 
  "This will return a list of movies of a specified tag --tag[tag_key_word]. This option works with --title",
  
  "--order" : 
  "This will return a list of movies of a specified tag --tag[tag_key_word]. This option works with --title and --by together",
  
  "--by" : 
  "This will return a list of movies of a specified tag --tag[tag_key_word]. This option works with --title and --by together",

}

# python3 movies_explorer --help
# python3 movies_explorer --title all --order desc --by [title a - z] [ genres a - z] [ rating a-z ...]
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
