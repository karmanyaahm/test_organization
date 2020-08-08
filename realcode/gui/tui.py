from .gui import gui
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import FuzzyWordCompleter, WordCompleter
from prompt_toolkit import PromptSession, print_formatted_text
from stringcase import titlecase
from realcode.functions import is_division
import os

### prompt stuff ###
DummyValidator = Validator.from_callable(lambda a: True, error_message="code broken")
DummyCompleter = WordCompleter([])


######TODO need to mvc
def status(mvc):
    dbHelper = mvc.dbHelper
    main_info = mvc.main_info

    dbHelper.reload()

    blocked = dbHelper.get_blocked(main_info.blocklistfile).blocked
    print(f"{len(blocked['c'])} div c invis blocked")
    print(f"{len(blocked['b'])} div b invis blocked")

    blocked = dbHelper.get_blocked(main_info.blocklistfile).public
    print(f"{len(blocked['c'])} div c invis public")
    print(f"{len(blocked['b'])} div b invis public")

    print(f"For more details look at {main_info.blocklistfile}")

    myeventlist, rotations = dbHelper.events.event_list, dbHelper.rotations
    print(f"{len(myeventlist)} events exist in the database")
    print(
        f"{len(rotations.keys())} individual events have rotations set up which are -- {', '.join([titlecase(i) for i in list(rotations.keys())])}"
    )
    print(f"For more details look at {main_info.eventlistfile}")


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


def randomtestarrange(
    term, locations,
):
    DivisionValidator = Validator.from_callable(
        is_division, error_message="Enter either b or c", move_cursor_to_end=True
    )
    div = term.prompt(
        "Division (b or c): ", validator=DivisionValidator, validate_while_typing=False
    ).strip()
    ## got division ##

    ### get list of events ###
    invis = mvc.getEventNameAutocomplete()

    ### ask for which event ###
    event_complete = FuzzyWordCompleter(invis)
    name = term.prompt(
        "Name: ", completer=event_complete, validator=DummyValidator
    ).strip()

    def is_year(yr):
        yr = "20" + yr
        return int(yr) < mvc.main_info.next_year and int(yr) > 2000

    ## ask for year ##
    YearValidator = Validator.from_callable(
        is_year,
        error_message=f"enter a number under {mvc.main_info.next_year} above 2000",
        move_cursor_to_end=True,
    )
    yr = term.prompt(
        "Year: 20", validator=YearValidator, validate_while_typing=False
    ).strip()
    # if someone uses this from like 2100 to 2110 you should probably fix this part to accomodate for the 90s

    mvc.randomtozip(mvc.main_info.wd + f"{name}-20{yr}/", div)


class tui(gui):
    def __init__(self, MVC):
        global mvc
        mvc = MVC
        self.mvc = MVC

    def start(self):
        self.term = PromptSession()
        term = self.term
        get_help()
        while 1:
            inp = term.prompt(
                "> ", validator=DummyValidator, completer=DummyCompleter
            ).strip()

            if inp == "1":
                randomtestarrange(term, locations=[])
            elif inp == "2":
                mvc.beyond_zipped()
                print("================ DONE ================")
            elif inp == "3":
                mvc.spreadsheet()
            elif inp == "4":
                status(mvc)
            elif inp == "h":
                get_help()
            elif inp == "q" or inp == "quit" or inp == "exit":
                print("================ BYE ================")
                mvc.leave(0)
            else:
                print("Wrong Input")

    def pause(self):
        self.term.prompt(
            "Fix files and press enter to continue",
            validator=DummyValidator,
            completer=DummyCompleter,
        )

