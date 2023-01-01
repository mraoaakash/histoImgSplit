from hashlib import md5
import shutil # for copying files
import os # for checking if file exists
import numpy as np # for image processing
import fnmatch # for matching file names
import uuid
import json

#  Global Variables
# out = "/storage/tnbc/dev-phase-001/histoimgsplit/OutputData_512/Mapping"
out = "/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/OutputData/Mapping"
# origin = "/storage/tnbc"
origin = "/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/testImage"
singletonout = {}
output = []

# Function that creates a unique key for each image
def keyer(image, impath):
    id = uuid.uuid4()
    return id

# Function that creates the name mapping from ICER to the new AU internal name 
def structurer(count, site="S01", locale="AU"):
    newname = f"{site}-{locale}-{str(count).zfill(6)}-R"
    newpath = os.path.join(out, newname)
    return newname, newpath

# Function that copies the image to the new folder with the new internal name
def copier(path, newpath, file):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        shutil.copy(path, f"{newpath}/{file}.tif")

# Function to create the metadata
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
    singletonout = {}
    counter+=1

# Saves the master metadata.json file
def masterjson():
    # if not os.path.exists(f"{out}/metadata.json"):
    #     pass
    # else:
    #     with open(f"{out}/metadata.json") as f:
    #         data = json.load(f)
    #         output.extend(data)
    json.dump(output, open(f"{out}/metadata.json", "w+"))

# Function that gets the image sources and calls all required supporter functions 
def imgRet(key='hne'):
    # list of folders to exclude
    # exclude = list(((open("/home/aakash.rao_ug23/cloud/histoImgSplit/patchGenerator/illfold.txt","r")).read().strip()).split(",")) 
    counter = 1
    for subdir, dirs, files in os.walk(origin):
        # dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if fnmatch.fnmatch(file, '*.tif'):
                if key in file.lower() and (("cropped" in file.lower())==False):
                    prpath=str(os.path.join(subdir, file))
                    datacreator(file, prpath, counter)
                    masterjson()
                    counter+=1

# Function that prints the progress of the script
def main():
    if not os.path.exists(out):
        os.makedirs(out)
    imgRet()

main()