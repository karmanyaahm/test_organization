import collections
from yaml import dump, load, FullLoader


class blocked:
    def __init__(self, content):
        self.public = []
        self.blocked = []
        self.filecontent = content
        self.parse()

    def __parse_mix(self, inp):
        def mix_bc(inp):
            if "bc" in inp.keys():
                bc = inp["bc"]
                inp["b"].update(bc)
                inp["c"].update(bc)
                inp.pop("bc")
            return inp

        def mix_year_and_set(inp):
            for t in [i for i in inp.keys() if not str(i).isdigit()]:
                inp[t] = set(inp[t])

            for year in [i for i in inp.keys() if str(i).isdigit()]:
                for t in inp[year]:
                    if t in inp.keys():
                        inp[t].add(year)
                    else:
                        inp[t] = set([year])
                inp.pop(year)

            return inp

        inp = mix_bc(inp)
        for div in "bc":
            inp[div] = mix_year_and_set(inp[div])
        return inp

    def __dict_merge(self, dct, merge_dct):
        """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
        updating only top-level keys, dict_merge recurses down into dicts nested
        to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
        ``dct``.
        :param dct: dict onto which the merge is executed
        :param merge_dct: dct merged into dct
        :return: None
        """
        for k, v in merge_dct.items():
            if (
                k in dct
                and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.abc.Mapping)
            ):
                dict_merge(dct[k], merge_dct[k])
            else:
                dct[k] = merge_dct[k]

    def __fancy_parse(self, blocked):
        for i in blocked.keys():
            for j in blocked[i]:
                if (
                    len(blocked[i][j]) == 0
                    or "*" == blocked[i][j]
                    or "*" in blocked[i][j]
                ):
                    blocked[i][j] = set(list(range(1984, 2050)))

    def parse(self):
        nt = load(self.filecontent, Loader=FullLoader)
        public = self.__parse_mix(nt["public"]).copy()
        blocked = self.__parse_mix(nt["not_trade"]).copy()

        self.__fancy_parse(public)
        self.__fancy_parse(blocked)

        self.public = public
        self.blocked = blocked

