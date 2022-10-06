from helpers.constants import MAIN_DICTIONARY
from helpers.utility_help import validate_comand
import argparse


def manage_user_input():
    parser = argparse.ArgumentParser("Line Comands Available")

    parser.add_argument('-t', '--title', type=str, help=MAIN_DICTIONARY["--title"])
    parser.add_argument('-g', '--genres', type=str, help=MAIN_DICTIONARY["--genres"])
    parser.add_argument('-r', '--rating', type=str, help=MAIN_DICTIONARY["--rating"])
    parser.add_argument('-l', '--tag', type=str, help=MAIN_DICTIONARY["--tag"])
    parser.add_argument('-d', '--release_date', type=str, help=MAIN_DICTIONARY["--release_date"])
    parser.add_argument('-o', '--order', type=str, help=MAIN_DICTIONARY["--order"])
    parser.add_argument('-b', '--by', type=str, help=MAIN_DICTIONARY["--by"])
    parser.add_argument('-c', '--count', action='store_true')

    args = parser.parse_args()
    dict_options_args = vars(args)

    validate_comand(dict_options_args)


manage_user_input()
