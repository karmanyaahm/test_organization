from yaml import dump, load, FullLoader


def events_from_dict(dictionary, path="."):
    for key, value in dictionary.items():
        if type(value) is dict:
            newpath = path + "/" + key
            if "rotations" in value.keys():
                yield (value, newpath)
            else:
                yield from events_from_dict(value, newpath)


def getfileslist(eventlistfile):
    fileslist = []

    rotations = {}

    cat = load(open(eventlistfile, "r").read(), Loader=FullLoader)
    for i, j in events_from_dict(cat):
        dirs = j.split("/")[1:]
        fileslist.append(
            (list(i["ids"]) if "ids" in i.keys() else [], dirs[-1], dirs[:-1])
        )
        if r := i["rotations"]:
            rotations[dirs[-1]] = r
    if __name__ == "__main__":
        print(len(fileslist))

    for n, i in enumerate(fileslist):
        i = list(i)
        i[0] = list(
            set(
                list(
                    i[0]
                    + [i[1]]
                    + [
                        i[1].replace("_", " "),
                        i[1].replace("_", ""),
                        i[1].replace(" ", ""),
                    ]
                )
            )
        )
        fileslist[n] = i
    return fileslist, rotations


# blocklist parser


def parse_mix(inp):
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


def get_blocked(blocklistfile):
    import collections

    def dict_merge(dct, merge_dct):
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

    nt = load(open(blocklistfile, "r").read(), Loader=FullLoader)
    notrade = parse_mix(nt["public"]).copy()
    dict_merge(notrade, parse_mix(nt["not_trade"]))
    return notrade


# if __name__ == "__main__":
#     from main import eventlistfile,blocklistfile
#     fileslist,rotations = getfileslist(eventlistfile)
#     blocked = get_blocked(blocklistfile)
