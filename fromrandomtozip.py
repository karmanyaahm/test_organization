import pwn as pwn
from difflib import SequenceMatcher
import glob
import stringcase
import shutil
import zipfile
import os
import re
from beyond_zippedlocations import start, initvars, delempty
from importlib import reload
import event_list
fileslist = event_list.fileslist
similarity_conf = 0.95

pat1 = '(?:[0-9]|\\b|_)('

pat2 = ')(?:[0-9]|\\b|_)'


class EventDoesNotExist(Exception):
    pass


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def getdirs():
    return [f.path for f in os.scandir('.') if f.is_dir()]


def getfiles():
    return [f.path for f in os.scandir('.') if f.is_file()]


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, _, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def remove_from_string(j, vars):
    for i in vars*50:
        j = j.replace(i, '')
    return j


def get_real_name(string):
    for i in fileslist:
        for j in [i[1]]+i[0]:
            if similar(j.lower(), string.lower()) >= similarity_conf or j.lower() in string.lower():
                return i[1]
    raise EventDoesNotExist


def removeParenthesis(j):
    try:
        int(j[-2])
        j = j[:-3]
    except:
        pass
    return j


def zipa():
    cut = 0
    fromback = 0
    for i in getdirs():
        try:
            j = i[2+cut:]
            j = remove_from_string(j, [' ', '_'])
            j = get_real_name(j)

        except EventDoesNotExist:
            print('no', j)
        # if inp:=input()!='':
        #     j = inp
        # print()
        else:
            name = f'{os.path.basename(os.getcwd())}-{j}-{div}.zip'

            with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipdir(i, zipf)
            shutil.rmtree(i)


def rename(renamenum, filename, newname):
    i = filename
    j = newname + i[renamenum:]
    shutil.move(i, j)
    print(j)


def rename_BorC():
    files = glob.glob('*.zip')
    for thefile in files:
        thefile = os.path.basename(thefile)
        shutil.move(thefile, thefile[:-5]+'b.zip')


def sortfolder():
    for j in fileslist:
        com = j[0]+[j[1]]
        j = j[1]
        for pos in com:
            files = [f for f in glob.glob(f'*',) if os.path.isfile(f)]
            for afile in files:
                pattern = pat1+pos.lower()+pat2
                if (re.search(pattern, os.path.basename(afile), re.IGNORECASE | re.MULTILINE)) and not (afile.split('.')[-1] == 'zip'):
                    os.makedirs(j, exist_ok=True)
                    shutil.move(afile, j)


def merge_same_name():
    for i in getdirs():
        to = i.lower().replace(' ', '').replace('_', '')
        if i != to:
            for thefile in glob.glob(i+'/*'):
                os.makedirs(to, exist_ok=True)
                shutil.move(thefile, to)


class getOutOfLoop(Exception):
    pass


name = 'kenston'
yr = 2018
wd = f'/home/karmanyaahm/data/oldstff/random/{name}-{yr}/'
div = 'c'

if __name__ == "__main__":
    os.chdir(wd)
    for _ in range(2):
        merge_same_name()
        delempty('.')

    for _ in range(3):
        if len([fi for fi in getfiles() if '.zip' not in fi]) > 0:
            merge_same_name()
            sortfolder()
            delempty('.')

            pwn.pause()

            event_list = reload(event_list)
            fileslist = event_list.fileslist
        else:
            break

    try:
        for _ in range(3):
            event_list = reload(event_list)
            fileslist = event_list.fileslist
            zipa()

            files = getfiles()+getdirs()
            allzip = True
            for i in files:
                if '.zip' not in i:
                    allzip &= False

            if allzip:
                break

            pwn.pause()

    except getOutOfLoop:
        pass
