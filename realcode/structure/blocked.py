class blocked:
    def __init__(self):
        self.public = []
        self.blocked = []
    def reload(self,file = None):
        if file:
            self.file = file
        self.parse()