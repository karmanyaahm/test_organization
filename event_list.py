fileslist = [(["score", "result", "scoring", "rank", "scores"],
              "score_report", ["other_idk", "score"],)]

fileslist += [
    (["fermi"], "fermi_questions", ["inquiry", "fermi"]),
    (["dynamic planet"], "dynamic_planet", ["earth_science", "dynamic_planet"]),
    (["forensic"], "forensics", ["chemistry", "forensics"]),
    (["disease"], "disease_detectives", ["biology", "disease"]),
    (["widi", "write_it"], "write_it_do_it", ["inquiry", "widi"]),
    (["mouse"], "mousetrap_vehicle", ["technology", "vehicle"]),
    (["mission possible", "possible"],
     "mission_possible", ["technology", "rube_goldberg"]),
    (["optics"], "optics", ["physics", "light"]),
    (["hover"], "hovercraft", ["technology", "vehicle"]),
    (["game"], "game_on", ["technology", "computer"]),
    (["codeb"], "codebusters", ["inquiry", "cryptography"]),
    (["sound"], "sounds_of_music", ["physics", "sound"]),
    (["fossil"], "fossils", ["earth_science", "fossil"]),
    (["water"], "water_quality", ["biology", "environment"]),
    (["designer", "genes"], "designer_genes", ["biology", "genetics"]),
    (["protein", "prot mod"], "protein_modelling", ["chemistry", "protein"]),
    (["circuit"], "circuit_lab", ["physics", "circuit"]),
    (["detector"], "detector_building", ["technology", "engineering"]),
    (["mapping", "geo map"], "geologic_mapping", ["earth_science", "geology"]),
    (["picture"], "picture_this", ["other_idk", "picture"]),
    (["machines"], "machines", ["physics", "energy"]),
    (["thermo"], "thermodynamics", ["physics", "energy"]),
    (["astron"], "astronomy", ["earth_science", "space"]),
    (["ornith"], "ornithology", ["biology", "bird"]),
    (["green", ], "green_generation", ["biology", "life_science"]),
    (["bowl"], "science_quiz_bowl", ["other_idk", "quiz_bowl"]),
    (["meme"], "lean_mean_meme_machine", ["dumb", "meme"]),
    (["botany"], "botany", ["biology", "plant"]),
    (["herpeto"], "herpetology", ["biology", "reptile"]),
    (["rocks_and_mineral", "mineral", "rocks"],
     "rocks_and_minerals", ["earth_science", "rocks"],),
    (["pokemon"], "pokemon_trivia", ["dumb", "pokemon"]),
    (["ecology"], "ecology", ["biology", "life_science"]),
    (["material", "matsci"], "material_science", ["chemistry", "materials"]),
    (["remote"], "remote_sensing", ["earth_science", "atmosphere"]),
    (["towers"], "towers", ["technology", "structure"]),
    (["boomilever"], "boomilever", ["technology", "structure"]),
    (["helicopters"], "helicopters", ["technology", "flying"]),
    (["hydrogeo", "hydogeolo"], "hydrogeology", ['earth_science', 'hydrosphere']),
    (["wind"], "wind_power", ['physics', 'wind']),
    (["microbe"], "microbe_mission", ["biology", "micro"]),
    (["invas"], "invasive_species", ["biology", "life_science"]),
    (["potions"], "potions_and_poisons", ['chemistry', 'potions']),
    (["solar sys", ], "solar_system", ["earth_science", "space"]),
    (["wright stuff"], "wright_stuff", ["technology", "flying"]),
    (["electric vehicle"], "electric_vehicle", ["technology", "vehicle"]),
    ([], "robot_arm", ['technology', 'robotics']),
    (["it_s about time", "about time"],
     "its_about_time", ['inquiry', 'timekeeping']),
    ([], "bridge_building", ["technology", "structure"]),
    (["cell bio", "cellbio"], "cell_biology", ["biology", "micro"]),
    ([], "source_code", ["technology", "computer"]),
    ([], "oceanography", ["earth_science", "ocean"]),
    ([], "pentathalon", ['other_idk', 'pentathalon']),
    ([], "air_trajectory", ["technology", "flying"]),
    ([], "entomology", ["biology", "life_science"]),
    (["tps", ], "technical_problem_solving", ['other_idk', 'tps']),
    (["compound machine"], "compound_machines", ["physics", "energy"]),
    ([], "maglev", ["technology", "vehicle"]),
    ([], 'solar_power', ['physics', 'energy']),
    ([], 'horticulture', ['biology', 'life_sciences']),
    ([], 'geocaching', ['other_idk', 'geocaching']),
    ([], 'data_science', ['inquiry', 'data_science']),
]

# probably b
fileslist += [
    (["road"], "road_scholar", ["earth_science", "mapping"]),
    (["meteor"], "meteorology", ['earth_science', 'atmosphere']),
    (["foodsci"], "food_science", ['chemistry', 'food']),
    (["fastfacts", "fast facts"], "fast_facts", ['other_idk', 'fast_facts']),
    ([], "density_lab", ['physics', 'density']),
    ([], "heredity", ['biology', 'genetics']),
    ([], "parasitology", ['biology', 'life_sciences']),
    ([], "duct_tape_challenge", ['inquiry', 'structure']),
    ([], "science_word", ['other_idk', 'word']),
]

fileslist += [
    # chem
    (["chem_lab", "chem lab", "chemlab", "chemistry lab"],
     "chemistry_lab", ["chemistry", "chemistry"],),
    (["crime"], "crime_busters", ["chemistry", "forensics"]),
    # bio
    (["anat", "a and p", "anatom", "a_p"],
     "anatomy_and_physiology", ["biology", "human"],),
    (["neursocience", "neuorscience"], "neuroscience", ['biology', 'human']),
    (["bio-process"], "bioprocess",
     ['biology', 'bioprocess_idk_where_this_should_go']),
    ([], "crave the wave", ['physics', 'waves']),
    ([], "forestry", ["biology", "life_science"]),
    # earth and stuff
    (["stars"], "reach_for_the_stars", ["earth_science", "space"]),
    # physics
    ([], "wifi_lab", ['physics', 'waves']),
    # tech
    ([], "algorithm_design", ['technology', 'computer']),
    # other
    ([], "geek_speak", ["dumb", "movies"]),
]
# build only idk why this needs to exist for tech
fileslist += [
    (["elglider"], "elastic_launch_glider", ["technology", "flying"]),
    ([], "battery_buggy", ["technology", "vehicle"]),
    ([], "roller_coaster", ['other_idk', 'roller_coaster']),
    ([], "gravity_vehicle", ["technology", "vehicle"]),
    (["ppp", "parachute"], "ping_pong_parachute", ["technology", "flying"]),
]
# like expd or mystery arch
fileslist += [
    (["mystery", "architecture"], "mystery_architecture", ['inquiry', 'structure']),
    (["exper", "expd", "exdes", "exp d", "xpd"],
     "experimental_design", ["inquiry", "experimental_design"],),


]


for n, i in enumerate(fileslist):
    i = list(i)
    i[0] = list(set(list(i[0] + [i[1]] + [i[1].replace("_", " "),
                                          i[1].replace("_", ""), i[1].replace(" ", "")])))
    fileslist[n] = i
if __name__ == "__main__":
    print(len(fileslist))

# anatomy people names
# fileslist=[
#     ([],'ohwell'),
#     ([],'annabeth'),
#     ([],'drcubbin'),
#     ([],'dulles'),
#     ([],'ninn'),
#     ([],'stjosephs'),
#     ([],'mrepithelium')


# ]


rotations = {
    'dynamic_planet': {
        'glacier': [2005, 2006, 2013, 2014, 2019],
        'ocean': [2007, 2008, 2015, 2016, 2020, 2021],
        'tectonics': [2009, 2010, 2017, 2018],
        'fresh_water': [2011, 2012],
    }
}
