import os


def getdirs():
    return [f.path for f in os.scandir('.') if f.is_dir()]

def delempty(dir):
    for i in [f[0] for f in os.walk(dir) if os.path.isdir(f[0])]:
        try:
            os.rmdir(i)
        except OSError:
            pass

