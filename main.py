#! /usr/bin/env python3.8

from __future__ import unicode_literals
import os

if os.name == "nt":
    print("use a real posix OS like mac or linux or bsd or something")
    exit(69)

from yaml import load, FullLoader
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import FuzzyWordCompleter, WordCompleter
from prompt_toolkit import PromptSession, print_formatted_text
from realcode.functions import is_division
from datetime import date
import sys
from realcode import listinvis, beyond_zippedlocations, fromrandomtozip, event_list
from stringcase import titlecase

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication


### prompt stuff ###
DummyValidator = Validator.from_callable(lambda a: True, error_message="code broken")
DummyCompleter = WordCompleter([])
root = os.path.dirname(os.path.realpath(__file__))
### listinvis ###
next_year = date.today().year + 1


config = load(open(root + "/config.yml", "r"), Loader=FullLoader)
blocklistfile = root + "/data/testtrade.yml"
eventlistfile = root + "/data/event_list.yml"

pat1 = "(?:[0-9]|\\b|_)("
pat2 = ")(?:[0-9]|\\b|_)"


similarity_conf = config["similarity_conf"]
spreadsheet_id = config["spreadsheet_id"]
maindir = config["maindir"]
start = maindir + "/tests/"
wd = maindir + "/random/"

dbHelper = event_list.DBHelper(eventlistfile, blocklistfile)


def spreadsheet():
    dbHelper.reload(blocklistfile=True)
    blocked = dbHelper.get_blocked()
    listinvis.main(start + "bylocation/", spreadsheet_id, next_year, blocked, root)


def beyond_zipped():
    beyond_zippedlocations.main(start, dbHelper)


def randomtozip(wd, div, thread):
    fromrandomtozip.main(dbHelper, wd, div, similarity_conf, pat1, pat2, start, thread)


def status():
    dbHelper.reload()

    blocked = dbHelper.get_blocked(blocklistfile).blocked
    print(f"{len(blocked['c'])} div c invis blocked")
    print(f"{len(blocked['b'])} div b invis blocked")

    blocked = dbHelper.get_blocked(blocklistfile).public
    print(f"{len(blocked['c'])} div c invis public")
    print(f"{len(blocked['b'])} div b invis public")

    print(f"For more details look at {blocklistfile}")

    myeventlist, rotations = dbHelper.events.event_list, dbHelper.rotations
    print(f"{len(myeventlist)} events exist in the database")
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


def randomtestarrange(term, locations, div, name, yr):
    # DivisionValidator = Validator.from_callable(
    #     is_division, error_message="Enter either b or c", move_cursor_to_end=True
    # )
    # div = term.prompt(
    #     "Division (b or c): ", validator=DivisionValidator, validate_while_typing=False
    # ).strip()
    # ## got division ##

    # ### get list of events ###
    # locations.append(os.getcwd())
    # os.chdir(start + "bylocation/")
    # invis = set(listinvis.getinvis("b")[0] + listinvis.getinvis("c")[0])
    # os.chdir(locations.pop())

    # ### ask for which event ###
    # event_complete = FuzzyWordCompleter(invis)
    # name = term.prompt(
    #     "Name: ", completer=event_complete, validator=DummyValidator
    # ).strip()

    # def is_year(yr):
    #     yr = "20" + yr
    #     return int(yr) < next_year and int(yr) > 2000

    # ## ask for year ##
    # YearValidator = Validator.from_callable(
    #     is_year,
    #     error_message=f"enter a number under {next_year} above 2000",
    #     move_cursor_to_end=True,
    # )
    # yr = term.prompt(
    #     "Year: 20", validator=YearValidator, validate_while_typing=False
    # ).strip()
    # # if someone uses this from like 2100 to 2110 you should probably fix this part to accomodate for the 90s

    randomtozip(wd + f"{name}-20{yr}/", div)


def main():
    global locations
    locations = []
    locations.append(os.getcwd())
    # term = PromptSession()
    # get_help()
    # while 1:

    #     inp = term.prompt(
    #         "> ", validator=DummyValidator, completer=DummyCompleter
    #     ).strip()

    #     if inp == "1":
    #         randomtestarrange(term, locations)
    #     elif inp == "2":
    #         beyond_zipped()
    #         print("================ DONE ================")

    #     elif inp == "3":
    #         spreadsheet()
    #     elif inp == "4":
    #         status()
    #     elif inp == "h":
    #         get_help()
    #     elif inp == "q" or inp == "quit" or inp == "exit":
    #         print("================ BYE ================")
    #         sys.exit(0)
    #     else:
    #         print("Wrong Input")
    app = QApplication(sys.argv)
    print(QtWidgets.QStyleFactory.keys())
    app.setStyle("Breeze")
    form = ExampleApp()
    form.show()
    app.exec_()
    os.chdir(locations.pop())


class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class randtozipthread(QThread):
    def __init__(self, div, eventname, year):
        self.div = div
        self.eventname = eventname
        self.year = year
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        try:
            randomtozip(wd + f"{self.eventname}-{self.year}/", self.div, self)
            print(f"{self.eventname}-{self.year} done")

        except FileNotFoundError:
            print(wd + f"{self.eventname}-{self.year}/")

    def pause(self):
        # print("pause")
        self.q_view_dlg = QtWidgets.QDialog()
        # print("2")
        self.q_view_dlg = uic.loadUi(root + "/realcode/gui/continue.ui")
        # print("3")
        self.q_view_dlg.exec_()


def getEventNameAutocomplete() -> list:
    locations.append(os.getcwd())
    os.chdir(start + "bylocation/")
    invis = set(listinvis.getinvis("b")[0] + listinvis.getinvis("c")[0])
    os.chdir(locations.pop())
    return list(invis)


class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)

        uic.loadUi("realcode/gui/gui.ui", self)
        sys.stdout = Stream(newText=self.onUpdateText)
        self.process = self.textEdit
        self.eventName.setCompleter(
            completer := QtWidgets.QCompleter(getEventNameAutocomplete())
        )
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

    def onUpdateText(self, text):
        cursor = self.process.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

    def __del__(self):
        sys.stdout = sys.__stdout__

    def randtozip(self):
        self.get_thread = randtozipthread(
            str(self.pickDiv.currentText()),
            str(self.eventName.text()),
            int(self.year.value()),
        )
        self.get_thread.start()

    def pressEnter(self):
        sys.stdin.write("\n")


if __name__ == "__main__":
    main()
