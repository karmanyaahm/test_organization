import os
from realcode import event_list
from realcode import listinvis, beyond_zippedlocations, fromrandomtozip, event_list


class GuiDoesNotExist(Exception):
    pass


class mvc:
    def __init__(self, main_info, gui):
        self.gui = self.__initGui(gui)
        self.dbHelper = event_list.DBHelper(
            main_info.eventlistfile, main_info.blocklistfile
        )
        self.main_info = main_info

    def __initGui(self, gui):
        if gui == "text":
            from realcode.gui.tui import tui

            raise GuiDoesNotExist
        elif gui == "qt":
            from realcode.gui.qt_gui import qt_gui

            return qt_gui()
        else:
            raise GuiDoesNotExist

    def start(self):
        self.gui.start(MVC=self)

    def pause(self):
        return self.gui.pause()

    def spreadsheet(self):
        self.dbHelper.reload(blocklistfile=True)
        blocked = self.dbHelper.get_blocked()
        listinvis.main(self.main_info.start + "bylocation/", self.main_info, blocked)

    def beyond_zipped(self):
        beyond_zippedlocations.main(self.main_info.start, self.dbHelper)

    def randomtozip(self, wd, div):
        fromrandomtozip.main( wd, div, self)

    def getEventNameAutocomplete(self,) -> list:
        main_info = self.main_info
        main_info.locations.append(os.getcwd())
        os.chdir(main_info.start + "bylocation/")
        invis = set(listinvis.getinvis("b")[0] + listinvis.getinvis("c")[0])
        os.chdir(main_info.locations.pop())
        return list(invis)

