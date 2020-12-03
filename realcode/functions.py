import os


def getdirs():
    return [f.path for f in os.scandir(".") if f.is_dir()]


def delempty(dir):
    for i in [f[0] for f in os.walk(dir) if os.path.isdir(f[0])]:
        try:
            os.rmdir(i)
        except OSError:
            pass


def is_division(text):
    return text.lower() == "b" or text.lower() == "c"


def getfiles():
    return [f.path for f in os.scandir(".") if f.is_file()]


# def rename(renamenum, filename, newname):
#     i = filename
#     j = newname + i[renamenum:]
#     shutil.move(i, j)
#     print(j)


# def rename_BorC():
#     files = glob.glob('*.zip')
#     for thefile in files:
#         thefile = os.path.basename(thefile)
#         shutil.move(thefile, thefile[:-5]+'b.zip')

def getzips(inpdir="."):
    return [
        os.path.basename(f.path)
        for f in os.scandir(inpdir)
        if ('.' in os.path.basename(f.path)) and os.path.basename(f.path).split(".")[1] == "test"
    ]

