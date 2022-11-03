from hashlib import md5
import shutil # for copying files
import os # for checking if file exists
import numpy as np # for image processing
import fnmatch # for matching file names
import uuid
import json


out = "./OutputFold/Mapping"
singletonout = {}
output = []

def keyer(image, impath):
    id = uuid.uuid4()
    return id

def structurer(count, site="S01", locale="AU"):
    newname = f"{site}-{locale}-{str(count).zfill(6)}-R"
    newpath = os.path.join(out, newname)
    return newname, newpath



def copier(path, newpath, file):
    print(singletonout)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        shutil.copy(path, f"{newpath}/{file}.tif")


def datacreator(file, prpath, counter):
    id = keyer(file,prpath)
    newname, newpath = structurer(counter)
    copier(prpath, newpath, newname)
    singletonout={
        'id':str(id),
        'newname':newname,
        'newpath':f'{newpath}/{newname}.tif',
        'srcpath':prpath,
        'srcname':file
    }
    output.append(singletonout)
    counter+=1

def masterjson():
    if not os.path.exists(f"{out}/master.json"):
        pass
    else:
        with open(f"{out}/master.json") as f:
            data = json.load(f)
            output.extend(data)
    json.dump(output, open(f"{out}/master.json", "w+"))
    print(output)

def imgRet(key='hne'):
    # list of folders to exclude
    # exclude = list(((open("/home/aakash.rao_ug23/cloud/histoImgSplit/illfold.txt","r")).read().strip()).split(",")) 
    exclude = ['clusters','ex_datasets','grand-challenge-data','segments','tSNE','benchmark','NewDatasetHnE','histoimgsplit']
    counter = 1
    for subdir, dirs, files in os.walk("./testImage"):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if fnmatch.fnmatch(file, '*.tif'):
                if key in file.lower() and (("cropped" in file.lower())==False):
                    prpath=str(os.path.join(subdir, file))
                    datacreator(file, prpath, counter)
                    masterjson()
                    counter+=1

def main():
    if not os.path.exists(out):
        os.makedirs(out)
    imgRet()

main()