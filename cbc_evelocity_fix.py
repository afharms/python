import os, shutil


opath = 'C:/Temp/Brothers Invoices/'
fpath = 'C:/Temp/Brothers Fixed/'
newline = ''

filelist = os.listdir(opath)

while(len(filelist) != 0):
    fname = filelist[0]
    with open(opath + fname, 'r') as f:
        contents = f.readlines()

    for line in contents:
        splits = line.split('\t')
        x = 0
        while x < len(splits):
            newline = newline + '~' + splits[x].rstrip()
            x+=1
        with open(fpath+fname, 'a') as f:
            f.write(newline[1:]+'\n')
        print(newline[1:])
        newline = ''
    filelist.remove(filelist[0])
