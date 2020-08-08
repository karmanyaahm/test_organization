from .gui import gui

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication
import sys


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
            mvc.randomtozip(main_info.wd + f"{self.eventname}-{self.year}/", self.div)
            print(f"{self.eventname}-{self.year} done")

        except FileNotFoundError:
            print(main_info.wd + f"{self.eventname}-{self.year}/")
        print("=======================")


class beyondzipthread(QThread):
    def __init__(self,):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        mvc.beyond_zipped()
        print("Arrange beyond zip done")
        print("=======================")


class spreadsheetupthread(QThread):
    def __init__(self,):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        mvc.spreadsheet()
        print("Spreadsheet upload done")
        print("=======================")


class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)

        uic.loadUi("realcode/gui/gui.ui", self)
        sys.stdout = Stream(newText=self.onUpdateText)
        self.process = self.textEdit
        self.eventName.setCompleter(
            completer := QtWidgets.QCompleter(mvc.getEventNameAutocomplete())
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

    def beyondzip(self):
        self.get_thread = beyondzipthread()
        self.get_thread.start()

    def spreadsheetup(self):
        self.get_thread = spreadsheetupthread()
        self.get_thread.start()


class qt_gui(gui):
    def start(self, MVC):
        global mvc, main_info
        mvc, main_info = MVC, MVC.main_info

        app = QApplication(sys.argv)
        # print(QtWidgets.QStyleFactory.keys())
        # app.setStyle("Breeze")
        form = ExampleApp()
        form.show()
        app.exec_()

    def pause(self):
        # print("pause")
        # print("2")
        q_view_dlg = uic.loadUi(main_info.root + "/realcode/gui/continue.ui")
        # print("3")
        q_view_dlg.exec_()

