from yaml import dump, load, FullLoader

# fileslist = [(["score", "result", "scoring", "rank", "scores"],
    #               "score_report", ["other_idk", "score"],)]

    # fileslist += [
    #     (["fermi"], "fermi_questions", ["inquiry", "fermi"]),
    #     (["dynamic planet", 'oceanography'], "dynamic_planet",
    #      ["earth_science", "dynamic_planet"]),
    #     (["forensic"], "forensics", ["chemistry", "forensics"]),
    #     (["disease", 'dd'], "disease_detectives", ["biology", "disease"]),
    #     (["widi", "write_it"], "write_it_do_it", ["inquiry", "widi"]),
    #     (["mouse"], "mousetrap_vehicle", ["technology", "vehicle"]),
    #     (["mission possible", "possible"],
    #      "mission_possible", ["technology", "rube_goldberg"]),
    #     (["optics"], "optics", ["physics", "light"]),
    #     (["hover"], "hovercraft", ["technology", "vehicle"]),
    #     (["game"], "game_on", ["technology", "computer"]),
    #     (["codeb"], "codebusters", ["inquiry", "cryptography"]),
    #     (["sound"], "sounds_of_music", ["physics", "sound"]),
    #     (["fossil"], "fossils", ["earth_science", "fossil"]),
    #     (["water"], "water_quality", ["biology", "environment"]),
    #     (["designer", "genes"], "designer_genes", ["biology", "genetics"]),
    #     (["protein", "prot mod"], "protein_modelling", ["chemistry", "protein"]),
    #     (["circuit"], "circuit_lab", ["physics", "circuit"]),
    #     (["detector"], "detector_building", ["technology", "engineering"]),
    #     (["mapping", "geo map"], "geologic_mapping", ["earth_science", "geology"]),
    #     (["picture"], "picture_this", ["other_idk", "picture"]),
    #     (["machines"], "machines", ["physics", "energy"]),
    #     (["thermo"], "thermodynamics", ["physics", "energy"]),
    #     (["astron"], "astronomy", ["earth_science", "space"]),
    #     (["ornith"], "ornithology", ["biology", "bird"]),
    #     (["green", ], "green_generation", ["biology", "life_science"]),
    #     (["bowl"], "science_quiz_bowl", ["other_idk", "quiz_bowl"]),
    #     (["meme"], "lean_mean_meme_machine", ["dumb", "meme"]),
    #     (["botany"], "botany", ["biology", "plant"]),
    #     (["herpeto"], "herpetology", ["biology", "reptile"]),
    #     (["rocks_and_mineral", "mineral", "rocks"],
    #      "rocks_and_minerals", ["earth_science", "rocks"],),
    #     (["pokemon"], "pokemon_trivia", ["dumb", "pokemon"]),
    #     (["ecology"], "ecology", ["biology", "life_science"]),
    #     (["material", "matsci", "materials"],
    #      "material_science", ["chemistry", "materials"]),
    #     (["remote"], "remote_sensing", ["earth_science", "atmosphere"]),
    #     (["towers"], "towers", ["technology", "structure"]),
    #     (["boomilever"], "boomilever", ["technology", "structure"]),
    #     (["helicopters"], "helicopters", ["technology", "flying"]),
    #     (["hydrogeo", "hydogeolo"], "hydrogeology", ['earth_science', 'hydrosphere']),
    #     (["wind"], "wind_power", ['physics', 'wind']),
    #     (["microbe"], "microbe_mission", ["biology", "micro"]),
    #     (["invas"], "invasive_species", ["biology", "life_science"]),
    #     (["potions"], "potions_and_poisons", ['chemistry', 'potions']),
    #     (["solar sys", ], "solar_system", ["earth_science", "space"]),
    #     (["wright stuff"], "wright_stuff", ["technology", "flying"]),
    #     (["electric vehicle"], "electric_vehicle", ["technology", "vehicle"]),
    #     ([], "robot_arm", ['technology', 'robotics']),
    #     (["it_s about time", "about time"],
    #      "its_about_time", ['inquiry', 'timekeeping']),
    #     ([], "bridge_building", ["technology", "structure"]),
    #     (["cell bio", "cellbio"], "cell_biology", ["biology", "micro"]),
    #     ([], "source_code", ["technology", "computer"]),
    #     ([], "pentathalon", ['other_idk', 'pentathalon']),
    #     ([], "air_trajectory", ["technology", "flying"]),
    #     ([], "entomology", ["biology", "life_science"]),
    #     (["tps", ], "technical_problem_solving", ['other_idk', 'tps']),
    #     (["compound machine"], "compound_machines", ["physics", "energy"]),
    #     ([], "maglev", ["technology", "vehicle"]),
    #     ([], 'solar_power', ['physics', 'energy']),
    #     ([], 'horticulture', ['biology', 'life_sciences']),
    #     ([], 'geocaching', ['other_idk', 'geocaching']),
    #     ([], 'data_science', ['inquiry', 'data_science']),
    # ]

    # # probably b
    # fileslist += [
    #     (["road"], "road_scholar", ["earth_science", "mapping"]),
    #     (["meteor"], "meteorology", ['earth_science', 'atmosphere']),
    #     (["foodsci"], "food_science", ['chemistry', 'food']),
    #     (["fastfacts", "fast facts"], "fast_facts", ['other_idk', 'fast_facts']),
    #     ([], "density_lab", ['physics', 'density']),
    #     ([], "heredity", ['biology', 'genetics']),
    #     ([], "parasitology", ['biology', 'life_sciences']),
    #     ([], "duct_tape_challenge", ['inquiry', 'structure']),
    #     ([], "science_word", ['other_idk', 'word']),
    # ]

    # fileslist += [
    #     # chem
    #     (["chem_lab", "chem lab", "chemlab", "chemistry lab"],
    #      "chemistry_lab", ["chemistry", "chemistry"],),
    #     (["crime"], "crime_busters", ["chemistry", "forensics"]),
    #     # bio
    #     (["anat", "a and p", "anatom", "a_p", "ap"],
    #      "anatomy_and_physiology", ["biology", "human"],),
    #     (["neursocience", "neuorscience"], "neuroscience", ['biology', 'human']),
    #     (["bio-process"], "bioprocess",
    #      ['biology', 'bioprocess_idk_where_this_should_go']),
    #     ([], "crave the wave", ['physics', 'waves']),
    #     ([], "forestry", ["biology", "life_science"]),
    #     # earth and stuff
    #     (["stars"], "reach_for_the_stars", ["earth_science", "space"]),
    #     # physics
    #     ([], "wifi_lab", ['physics', 'waves']),
    #     # tech
    #     ([], "algorithm_design", ['technology', 'computer']),
    #     # other
    #     ([], "geek_speak", ["dumb", "movies"]),
    # ]
    # # build only idk why this needs to exist for tech
    # fileslist += [
    #     (["elglider"], "elastic_launch_glider", ["technology", "flying"]),
    #     ([], "battery_buggy", ["technology", "vehicle"]),
    #     ([], "roller_coaster", ['other_idk', 'roller_coaster']),
    #     ([], "gravity_vehicle", ["technology", "vehicle"]),
    #     (["ppp", "parachute"], "ping_pong_parachute", ["technology", "flying"]),
    # ]
    # # like expd or mystery arch
    # fileslist += [
    #     (["mystery", "architecture"], "mystery_architecture", ['inquiry', 'structure']),
    #     (["exper", "expd", "exdes", "exp d", "xpd"],
    #      "experimental_design", ["inquiry", "experimental_design"],),
    # ]

    # # anatomy people names
    # # fileslist=[
    # #     ([],'ohwell'),
    # #     ([],'annabeth'),
    # #     ([],'drcubbin'),
    # #     ([],'dulles'),
    # #     ([],'ninn'),
    # #     ([],'stjosephs'),
    # #     ([],'mrepithelium')

    # # ]

    # example_toml = '''
    # [[biology]]

    #     [[biology.human]]
    #         name = "anatomy_and_physiology"
    #         ids = [
    #             "a_p",
    #             "anatomy",
    #         ]
    #         rotate = true
    #         [[biology.human.anatomy_and_physiology.rotations]]
    #             "skeletal-muscular-integumentary" = [2016, 2020]

    # '''

    # example_yaml = '''
    # - biology:
    #     - human:
    #         - name: anatomy_and_physiology
    #           ids:
    #             - a_p
    #             - anatomy
    #           rotate: True
    #           rotations:
    #             - skeletal-muscular-integumentary:  [2016, 2020]
    # '''
    # rrotations = {
    #     'dynamic_planet': {
    #         'glacier': [2005, 2006, 2013, 2014, 2019],
    #         'ocean': [2007, 2008, 2015, 2016, 2020, 2021],
    #         'tectonics': [2009, 2010, 2017, 2018],
    #         'fresh_water': [2011, 2012],
    #     },
    #     'anatomy_and_physiology': {
    #         'skeletal-muscular-integumentary': [2016, 2020],
    #         'cardiovascular-lymphatic-excretory': [2019],
    #         'respiratory-digestive-immune': [2018],
    #         'nervous-sense_organs-endocrine': [2017],
    #         'cardiovascular-integumentary-immune': [2015],
    #         'integumentary-Nervous-immune(c)': [2014],
    #         'nervous-digestive-excretory(c)': [2013],
    #         'digestive-respiratory-excretory(c)': [2012],
    #         'respiratory-muscular-endocrine(c)': [2011],
    #         'muscular-skeletal-endocrine(c)': [2010],
    #         'skeletal-circulatory-?': [2009],
    #         'circulatory-nervous-?': [2008],
    #     },
    # }


###good stuff####
def events_from_dict(dictionary, path='.'):
    for key, value in dictionary.items():
        if type(value) is dict:
            newpath = path+'/'+key
            if 'rotations' in value.keys():
                yield (value, newpath)
            else:
                yield from events_from_dict(value, newpath)





def getfileslist(eventlistfile):
    fileslist = []

    rotations = {}

    cat = load(open(eventlistfile, 'r').read(),Loader=FullLoader)
    for i, j in events_from_dict(cat):
        dirs = j.split('/')[1:]
        fileslist.append(
            (list(i['ids']) if 'ids' in i.keys() else [], dirs[-1], dirs[:-1]))
        if r:= i['rotations']:
            rotations[dirs[-1]] = r
    if __name__ == "__main__":
        print(len(fileslist))


    for n, i in enumerate(fileslist):
        i = list(i)
        i[0] = list(set(list(i[0] + [i[1]] + [i[1].replace("_", " "),
                                            i[1].replace("_", ""), i[1].replace(" ", "")])))
        fileslist[n] = i
    return fileslist,rotations



###blocklist parser

def parse_mix(inp):

    def mix_bc(inp):
        if 'bc' in inp.keys():
            bc = inp['bc']
            inp['b'].update(bc)
            inp['c'].update(bc)
            inp.pop('bc')
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
    for div in 'bc':
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
            if (k in dct and isinstance(dct[k], dict)
                    and isinstance(merge_dct[k], collections.abc.Mapping)):
                dict_merge(dct[k], merge_dct[k])
            else:
                dct[k] = merge_dct[k]

    nt = load(open(blocklistfile, 'r').read(), Loader=FullLoader)
    notrade = parse_mix(nt['public']).copy()
    dict_merge(notrade, parse_mix(nt['not_trade']))
    return notrade


# if __name__ == "__main__":
#     from main import eventlistfile,blocklistfile
#     fileslist,rotations = getfileslist(eventlistfile)
#     blocked = get_blocked(blocklistfile)