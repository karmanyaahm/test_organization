import listinvis
import beyond_zippedlocations
import fromrandomtozip


### listinvis ###
next_year = 2021
spreadsheet_id = '1EI_McY52x9RBUgShYJZFVzeEW4KCsFKS5ByjgUCFkgM'
# spreadsheet_id = '15rfL6gtEmJnbaUnR-q320swX9kvOyunpneYIsupRNNQ' #for testing

### rand to zip ###
similarity_conf = 0.95
pat1 = '(?:[0-9]|\\b|_)('
pat2 = ')(?:[0-9]|\\b|_)'
###
eventlistfile = '/home/karmanyaahm/data/oldstff/tests/scripts/event_list.yml'


def spreadsheet():
    from event_list import get_blocked
    blocked = get_blocked()
    listinvis.main(start + 'bylocation/', spreadsheet_id, next_year,blocked)


def beyond_zipped():
    beyond_zippedlocations.main(eventlistfile, start)


def randomtozip(wd):
    fromrandomtozip.main(eventlistfile, wd, div,
                         similarity_conf, pat1, pat2, start)


start = '/home/karmanyaahm/data/oldstff/tests/'


name = 'mentor'
yr = 16
div = 'c'
wd = f'/home/karmanyaahm/data/oldstff/random/{name}-20{yr}/'

def main():
    while 1:
        print('''
        1 - Random test arrangement to zip
        2 - arrange beyond zipped
        3 - spreadsheet upload
        ''')
        inp = input("> ").strip()
        if inp == '1':
            name = input("Name: ").strip()
            good = 0
            while not good:
                yr = input("Year: 20").strip()
                try:
                    assert int(yr) < next_year and int(yr) > 0 #if someone uses this from like 2100 to 2110 you should probably fix this part to accomadate for the 90s
                    good = 1
                except:
                    print(f"enter a number under {next_year}")
                    pass
            good = 0
            while not good:
                div = input("Division (b or c): ").strip()
                try:
                    assert div =='b' or div =='c'
                    good = 1
                except:
                    print("enter either b or c")
                    pass
            wd = f'/home/karmanyaahm/data/oldstff/random/{name}-20{yr}/'

            randomtozip(wd)

        elif inp == '2':
            beyond_zipped()
        elif inp == '3':
            spreadsheet()
        elif inp =='q' or inp =='quit' or inp =='exit':
            print("================ BYE ================")
            exit(0)
        print("================ DONE ================")



if __name__ == "__main__":
    main()