class event:
    def __init__(self, name: str, category: list, ids: int):
        self.name = name
        self.category = category
        self.set_ids(ids)

    def set_ids(self, ids):
        """
        Set name before calling this in init
        """
        name = self.name
        ids = list(
            set(
                ids
                + [
                    name,
                    name.replace("_", " "),
                    name.replace("_", ""),
                    name.replace(" ", ""),
                ]
            )
        )
        self.ids = ids

    @classmethod
    def from_old(cls, inp):
        return cls(name=inp[1], category=inp[2], ids=inp[0])

    def get_old(self):
        return [self.ids, self.name, self.category]

