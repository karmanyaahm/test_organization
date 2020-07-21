from .functions import getdirs,delempty,getfiles
import pwn as pwn
from difflib import SequenceMatcher
import glob
import stringcase
import shutil
import zipfile
import os
import re
from .event_list import getfileslist


class EventDoesNotExist(Exception):
    pass


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()




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
            print('no', j,'event')
        # if inp:=input()!='':
        #     j = inp
        # print()
        else:
            name = f'{os.path.basename(os.getcwd())}-{j}-{div}.zip'

            with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipdir(i, zipf)
            shutil.rmtree(i)



def sortfolder():
    for j in fileslist:
        com = j[0]+[j[1]]
        j = j[1]
        for pos in com:
            files = [f for f in glob.glob(f'*',) if os.path.isfile(f)]
            for afile in files:
                if len(pos) < 6:
                    pattern = pat1+pos.lower()+pat2
                else:
                    pattern = pat1+'.*'+pos.lower()+'.*'+pat2
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


def main(eventlistfile,wd, Div, Similarity_conf, Pat1, Pat2,start):
    cwd = os.getcwd()
    global fileslist,pat1,pat2,similarity_conf,div
    pat1,pat2,similarity_conf,div = Pat1,Pat2,Similarity_conf,Div
    fileslist,rotations = getfileslist(eventlistfile)
    os.chdir(wd)
    for _ in range(2):
        merge_same_name()
        delempty('.')

    for _ in range(100):
        if len([fi for fi in getfiles() if '.zip' not in fi]) > 0:
            merge_same_name()
            sortfolder()
            delempty('.')

            pwn.pause()

            fileslist,rotations = getfileslist(eventlistfile)
        else:
            break

    try:
        for _ in range(100):
            fileslist,rotations = getfileslist(eventlistfile)
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
    os.chdir(cwd)


# if __name__ == "__main__":
#     from main import eventlistfile,wd, div, similarity_conf, pat1, pat2,start
#     main(eventlistfile,wd, div, similarity_conf, pat1, pat2,start)