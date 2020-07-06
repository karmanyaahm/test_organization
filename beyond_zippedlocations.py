import re
import shutil
import zipfile
import os
import glob
from event_list import fileslist,rotations


start = '/home/karmanyaahm/data/oldstff/tests/'


def initvars(divi):
    global byevent
    global testroot
    global div
    byevent = f'byevent-{divi}/'
    testroot = 'actualtests/'
    div = divi


def delempty(dir):
    for i in [f[0] for f in os.walk(dir) if os.path.isdir(f[0])]:
        try:
            os.rmdir(i)
        except OSError:
            pass


def move():
    todir = f'byevent-{div}/'
    for j in fileslist:
        k = j[1]
        j = j[0]
        ki = byevent + k
        os.makedirs(ki, exist_ok=True)
        for ji in j:
            files = glob.glob(
                f'bylocation/good-{div}/*/*{ji}*', recursive=True)
            for i in files:
                try:
                    os.symlink(f'../../{i}', byevent +
                               f'{k}/{os.path.split(i)[1]}')
                except FileExistsError:
                    pass


def moveback():
    # for thefile in glob.glob(f'byevent-{div}/**/*.zip', recursive=True):
    #     thefilen = os.path.split(thefile)[1]
    #     event = thefilen.split('-')
    #     event = f'{event[0]}-{event[1]}'
    #     os.makedirs(f'bylocation/good-{div}/'+event+'/', exist_ok=True)
    #     shutil.move(thefile, f'bylocation/good-{div}/'+event+'/')
    pass  # hopefully won't have to use this again


def symlink():
    for j in fileslist:
        if len(j) == 3:
            j, k, l = j
            todir = testroot + f'{l[0]}/{l[1]}/{div}/'
            fromdir = byevent+k
            if len(os.listdir(fromdir)) > 0:
                os.makedirs(todir, exist_ok=True)
                try:
                    os.symlink('../../../../'+fromdir, todir+f'{k}')
                except FileExistsError:
                    pass
        else:
            print(f'update {j[1]}')


def getzips(inpdir='.'):
    return [os.path.basename(f.path) for f in os.scandir(inpdir) if f.is_file() and os.path.basename(f.path).split('.')[1] == 'zip' ]

def get_category_from_year(event,year):
    for j,k in rotations[event].items():
        if year in k: return j

def dorotations():
    for event in rotations.keys():
        todir = f'byevent-{div}/{event}'
        if os.path.isdir(todir):
            os.chdir(todir)
            zips = getzips()
            for category in rotations[event].keys():
                os.makedirs('by_category-'+category,exist_ok=True)
            for thiszip in getzips():
                cat = 'by_category-' + get_category_from_year(event, int(thiszip.split('-')[1]))
                try:
                    os.symlink('../'+thiszip,cat+'/'+thiszip)
                except FileExistsError:
                    pass
            
            os.chdir('../..')




def main():
    for i in ['c', 'b']:
        initvars(i)
        move()
        dorotations()
        symlink()


if __name__ == "__main__":
    os.chdir(start)
    delempty('.')

    main()

    delempty('.')
