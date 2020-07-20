
from __future__ import unicode_literals
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit import PromptSession, print_formatted_text
import listinvis
import beyond_zippedlocations
import fromrandomtozip
from functions import is_division
from datetime import date


import os
### listinvis ###
next_year = date.today().year+1

### rand to zip ###
similarity_conf = 0.95
pat1 = '(?:[0-9]|\\b|_)('
pat2 = ')(?:[0-9]|\\b|_)'
###

# name = 'mentor'
# yr = 16
# div = 'c'


def spreadsheet():
    from event_list import get_blocked
    blocked = get_blocked()
    listinvis.main(start + 'bylocation/', spreadsheet_id, next_year, blocked)


def beyond_zipped():
    beyond_zippedlocations.main(eventlistfile, start)


def randomtozip(wd, div):
    fromrandomtozip.main(eventlistfile, wd, div,
                         similarity_conf, pat1, pat2, start)


def randomtestarrange():
    DivisionValidator = Validator.from_callable(
        is_division, error_message='Enter either b or c', move_cursor_to_end=True)
    div = term.prompt(
        "Division (b or c): ", validator=DivisionValidator, validate_while_typing=False).strip()

    locations.append(os.getcwd())
    os.chdir(start+'bylocation/')
    invis = set(listinvis.getinvis('b')[0]+listinvis.getinvis('c')[0])
    os.chdir(locations.pop())

    event_complete = FuzzyWordCompleter(invis)
    name = term.prompt("Name: ", completer=event_complete, validator=Validator.from_callable(
        lambda a: True, error_message='code broken')).strip()

    def is_year(yr):
        yr = '20'+yr
        return (int(yr) < next_year and int(yr) > 2000)

    YearValidator = Validator.from_callable(
        is_year, error_message=f"enter a number under {next_year} above 2000", move_cursor_to_end=True)

    yr = term.prompt("Year: 20", validator=YearValidator,
                     validate_while_typing=False).strip()
    # if someone uses this from like 2100 to 2110 you should probably fix this part to accomodate for the 90s

    randomtozip(wd+f'{name}-20{yr}/', div)


eventlistfile = '/home/karmanyaahm/data/oldstff/tests/scripts/event_list.yml'
spreadsheet_id = '1EI_McY52x9RBUgShYJZFVzeEW4KCsFKS5ByjgUCFkgM'
# spreadsheet_id = '15rfL6gtEmJnbaUnR-q320swX9kvOyunpneYIsupRNNQ' #for testing

start = '/home/karmanyaahm/data/oldstff/tests/'


wd = f'/home/karmanyaahm/data/oldstff/random/'


def main():

    locations = []
    locations.append(os.getcwd())
    term = PromptSession()
    while 1:

        print_formatted_text('''
        1 - Random test arrangement to zip
        2 - arrange beyond zipped
        3 - spreadsheet upload
        ''')
        inp = term.prompt("> ").strip()

        if inp == '1':
            randomtestarrange()
        elif inp == '2':
            beyond_zipped()
        elif inp == '3':
            spreadsheet()
        elif inp == 'q' or inp == 'quit' or inp == 'exit':
            print("================ BYE ================")
            exit(0)
        print("================ DONE ================")
    os.chdir(locations.pop())


if __name__ == "__main__":
    main()
