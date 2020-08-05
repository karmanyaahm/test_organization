from yaml import dump, load, FullLoader
from realcode.structure.event import event
from realcode.structure.events import events
from realcode.structure.blocked import blocked

# blocklist parser


class DBHelper:
    def __init__(self, eventlistfile, blocklistfile):
        self.reload(eventlistfile=eventlistfile, blocklistfile=blocklistfile)

    def reload(self, eventlistfile=False, blocklistfile=False):
        if not eventlistfile and not blocklistfile:
            self.reload(eventlistfile=True, blocklistfile=True)

        if eventlistfile == True:
            self.eventlistfilecontents = open(self.eventlistfile, "r").read()
            self.parse_event_list()
        elif eventlistfile:
            self.eventlistfile = eventlistfile
            self.reload(eventlistfile=True)

        if blocklistfile == True:
            self.blocklistfilecontents = open(self.blocklistfile, "r").read()
            self.blocked = blocked(self.blocklistfilecontents)
        elif blocklistfile:
            self.blocklistfile = blocklistfile
            self.reload(blocklistfile=True)

    ### internal functions ###
    def __events_from_dict(self, dictionary, path="."):
        for key, value in dictionary.items():
            if type(value) is dict:
                newpath = path + "/" + key
                if "rotations" in value.keys():
                    yield (value, newpath)
                else:
                    yield from self.__events_from_dict(value, newpath)

    ### main things ###
    def parse_event_list(self):
        myevents = events()
        rotations = {}
        cat = load(self.eventlistfilecontents, Loader=FullLoader)

        for i, j in self.__events_from_dict(cat):
            dirs = j.split("/")[1:]
            myevents.append(
                event(dirs[-1], dirs[:-1], list(i["ids"]) if "ids" in i.keys() else [],)
            )
            if r := i["rotations"]:
                rotations[dirs[-1]] = r
        if __name__ == "__main__":
            print(len(fileslist))

        self.events = myevents
        self.rotations = rotations

    ### legacy compatibility ###

    def get_blocked(self, blocklistfile="lol"):
        return self.blocked


# db = DBHelper("data/event_list.yml", "data/testtrade.yml")
# db.parse_event_list()

# if __name__ == "__main__":
#     from main import eventlistfile,blocklistfile
#     fileslist,rotations = getfileslist(eventlistfile)
#     blocked = get_blocked(blocklistfile)

