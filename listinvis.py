import os
import shutil
import difflib
from fromrandomtozip import getdirs


next_year = 2021

start = '/home/karmanyaahm/data/oldstff/tests/bylocation/'

os.chdir(start)
div = 'c'

for div in ['b','c']:
    og = f'/home/karmanyaahm/data/oldstff/tests/scripts/invis_list-{div}new.csv'
    new  = f'/home/karmanyaahm/data/oldstff/tests/scripts/invis_list-{div}.csv'
    try: shutil.move(new,og)
    except FileNotFoundError: open(og,'w').write('')

    os.chdir(f'good-{div}')

    dirs = [dir[2:] for dir in getdirs()]

    os.chdir('..')




    #print(dirs)


    dirs = [this.split('-') for this in dirs]
    oldest = 2100
    for d,f in dirs:
        oldest = min(int(f),int(oldest))

    invis = sorted(list(set([d[0] for d in dirs])))

    write = []


    for i in invis:
        arr = []
        for d in dirs:
            if d[0] == i:
                arr.append(d[1])
        write.append([i, set(arr)])
    for n,w in enumerate(write):
        arr = []
        for i in range(oldest,next_year):
            arr.append(1 if str(i) in w[1] else 0)
        write[n]=[w[0]]+list(arr)

    write.insert(0,['invi',]+list(range(oldest,next_year)))


    with open(new, 'w') as f:
        for w in write:
            f.write(','.join([str(ww) for ww in w])+'\n')
    print(div)
    print(','.join([str(i)[2:] for i in write[0][1:]]))
    for line in difflib.unified_diff(open(og,'r').readlines() ,open(new,'r').readlines(), fromfile='old', tofile='new', lineterm='', n=0):
        for prefix in ('---', '+++', '@@'):
            if line.startswith(prefix):
                break
        else:
            print(line,)
        # print(line)
    os.remove(og)

div = 'b'