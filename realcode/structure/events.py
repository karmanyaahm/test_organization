from realcode.structure.event import event


class events:
    def __init__(self):
        self.event_list = []

    def append(self, thing: event):
        self.event_list.append(thing)

    def get_event_list(self):
        return self.event_list

