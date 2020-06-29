# run from the tests dir
import os

topics = {'biology': ['anatomy_and_physiology',
                        'designer_genes','disease_detectives','ornithology','water_quality'],
          'physics': ['circuit_lab','machines','sounds_of_music'],
          'chemistry':['chem_lab']

          }

def makedir(thing,dirname):
    newpath = thing 
    if not os.path.exists(newpath):
        os.makedirs(newpath)


for topic,events in topics.items():
    upper1 = '.'
    new1 = topic
    makedir(new1,upper1)
    os.chdir(new1)
    for event in events:
        upper2 = new1
        new2 = f"{event}"
        makedir(new2,upper2)
        os.chdir(new2)
        for division in ['b','c']:
            upper3 = new2
            new3 = f"{division}"
            makedir(new3,upper3)
            os.chdir(new3)
            for year in range(2010,2021):
                upper4 = new3
                new4 = f"{year}"
                makedir(new4,upper4)
            os.chdir('..')
        os.chdir('..')
    os.chdir('..')


