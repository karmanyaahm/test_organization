#! /usr/bin/env python3.8

from __future__ import unicode_literals
import os

if os.name == "nt":
    print("use a real posix OS like mac or linux or bsd or something")
    exit(69)

from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit import PromptSession, print_formatted_text
from realcode.functions import is_division
from datetime import date
import sys
from realcode import listinvis, beyond_zippedlocations, fromrandomtozip, event_list
from stringcase import titlecase

### prompt stuff ###
DummyValidator = Validator.from_callable(lambda a: True, error_message="code broken")
root = os.path.realpath(sys.path[0])
blocklistfile = root + "/data/testtrade.yml"
eventlistfile = root + "/data/event_list.yml"

### listinvis ###
next_year = date.today().year + 1

### rand to zip ###
similarity_conf = 0.95
pat1 = "(?:[0-9]|\\b|_)("
pat2 = ")(?:[0-9]|\\b|_)"
###

# name = 'mentor'
# yr = 16
# div = 'c'


def spreadsheet():
    blocked = event_list.get_blocked(blocklistfile)
    listinvis.main(start + "bylocation/", spreadsheet_id, next_year, blocked, root)


def beyond_zipped():
    beyond_zippedlocations.main(eventlistfile, start)


def randomtozip(wd, div):
    fromrandomtozip.main(eventlistfile, wd, div, similarity_conf, pat1, pat2, start)


def status():
    blocked = event_list.get_blocked(blocklistfile)
    print(f"{len(blocked['c'])} div c invis blocked")
    print(f"{len(blocked['b'])} div b invis blocked")
    print(f"For more details look at {blocklistfile}")
    fileslist, rotations = event_list.getfileslist(eventlistfile)
    print(f"{len(fileslist)} events exist in the database")
    print(
        f"{len(rotations.keys())} individual events have rotations set up which are -- {', '.join([titlecase(i) for i in list(rotations.keys())])}"
    )
    print(f"For more details look at {eventlistfile}")


def get_help():
    print_formatted_text(
        """
        1 - Random test arrangement to zip
        2 - arrange beyond zipped
        3 - spreadsheet upload
        4 - status (wip)
        h - help
        q - quit
        """
    )


def randomtestarrange(term, locations):
    DivisionValidator = Validator.from_callable(
        is_division, error_message="Enter either b or c", move_cursor_to_end=True
    )
    div = term.prompt(
        "Division (b or c): ", validator=DivisionValidator, validate_while_typing=False
    ).strip()
    ## got division ##

    ### get list of events ###
    locations.append(os.getcwd())
    os.chdir(start + "bylocation/")
    invis = set(listinvis.getinvis("b")[0] + listinvis.getinvis("c")[0])
    os.chdir(locations.pop())

    ### ask for which event ###
    event_complete = FuzzyWordCompleter(invis)
    name = term.prompt(
        "Name: ", completer=event_complete, validator=DummyValidator
    ).strip()

    def is_year(yr):
        yr = "20" + yr
        return int(yr) < next_year and int(yr) > 2000

    ## ask for year ##
    YearValidator = Validator.from_callable(
        is_year,
        error_message=f"enter a number under {next_year} above 2000",
        move_cursor_to_end=True,
    )
    yr = term.prompt(
        "Year: 20", validator=YearValidator, validate_while_typing=False
    ).strip()
    # if someone uses this from like 2100 to 2110 you should probably fix this part to accomodate for the 90s

    randomtozip(wd + f"{name}-20{yr}/", div)


spreadsheet_id = "1EI_McY52x9RBUgShYJZFVzeEW4KCsFKS5ByjgUCFkgM"
# spreadsheet_id = '15rfL6gtEmJnbaUnR-q320swX9kvOyunpneYIsupRNNQ' #for testing

maindir = "/home/karmanyaahm/data/oldstff"

start = maindir + "/tests/"


wd = maindir + "/random/"


def main():
    locations = []
    locations.append(os.getcwd())
    term = PromptSession()
    get_help()
    while 1:

        inp = term.prompt("> ", validator=DummyValidator).strip()

        if inp == "1":
            randomtestarrange(term, locations)
        elif inp == "2":
            beyond_zipped()
            print("================ DONE ================")

        elif inp == "3":
            spreadsheet()
        elif inp == "4":
            status()
        elif inp == "h":
            get_help()
        elif inp == "q" or inp == "quit" or inp == "exit":
            print("================ BYE ================")
            exit(0)
        else:
            print("Wrong Input")
    os.chdir(locations.pop())


if __name__ == "__main__":
    main()
