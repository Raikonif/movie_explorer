# MOVIES EXPLORER



THIS APPLICACION IS A COMMAND LINE UTILITY TOOL THAT HELPS US QUERY MOVIE DATA.

QUERY RESPONSE ARE PRINTED IN THE STANDARD OUTPUT, AN ALSO GENERATE AN OUTPUT FILE



## RECOMMENDATIONS



-   PYTHON VERSION RECOMMENDED 3.9.14



## DESCRIPTION



For the user to launch the application must type different kind of available command line inputs,

you can type "python app.py --help"



## **python app.py --help output**



-h, --help            show this help message and exit

  -t N, --title N       this function returns a list of movies. Insert "all" to return all the database, or specify the name of the wantde movie.

                        Regex available. You can use it with "--sort" "by"

  -g GENRES, --genres GENRES

                        This will return a response that have movies that have the same genre

  -r RATING, --rating RATING

                        This comand show all movies that have the specified rating

  -l TAG, --tag TAG     This return something that I dont understand TODO

  -d RELEASE_DATE, --release_date RELEASE_DATE

                        This only works with title

  -o ORDER, --order ORDER

                        This only works with title

  -b BY, --by BY        This only works with title