import tifffile as tf
import os
import uuid
import json
import shutil
import cv2


# Global Variables
singletonout = {}
currentimg = {}
# out = "/storage/tnbc/dev-phase-001/histoimgsplit/OutputData_512/Mapping"
# ids = "/storage/tnbc/dev-phase-001/histoimgsplit/OutputData_512/DataSet"
out  = "/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/OutputData/Mapping"
ids = "/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/OutputData/DataSet"

# Json object
IDJSON = []

# Reprinter Function
_last_print_len = 0 
def reprint(msg, finish=False): 
    global _last_print_len 
     
    print(' '*_last_print_len, end='\r') 
     
    if finish: 
        end = '\n' 
        _last_print_len = 0 
    else: 
        end = '\r' 
        _last_print_len = len(msg) 
     
    print(msg, end=end) 

# Function that reads the created metadata.json and copies the images to the dataset folder keyed by UUID
def idcopy(size):
    reprint(f"Creating ID json for size = {size} along with ID folder")
    idpath = f"{ids}/{size//35}x"
    jsonspath = f"{idpath}/jsons"
    if not os.path.exists(idpath):
            os.makedirs(idpath)
    if not os.path.exists(jsonspath):
            os.makedirs(jsonspath)
    for i in LOCALJSON:
        shutil.copyfile(f"{i['patchpath']}", f"{idpath}/{i['id']}.tif")
        partition = {
            'name': f"{i['id']}.tif",
            'id': i['id'],
            'patchpath': f"{idpath}/{i['id']}.tif",
            'srcname': i['srcname'],
            'srcpath': i['patchpath'],
            'size': i['size']
        }
        IDJSON.append(partition)
        json.dump(partition, open(f"{jsonspath}/{i['id']}.json", "w+"))
    reprint(f"ID folder and jsons created")


# Creates the original metadata.json
def metadatawriter(size):
    print(f"Creating local json for size = {size}")
    jspath = f"{out}/{currentimg['newname']}/{size//35}x/metadata.json"
    json.dump(LOCALJSON, open(jspath, "w+"))
    idcopy(size)
    print(f"Finished creating local json for size = {size}")

# Function that takes the input from the master metadata.json 
def inputter():
    print(f"Getting Image Sources")
    with open(f'{out}/metadata.json') as f:
        data = json.load(f)
    global sourcelist 
    sourcelist = data

# Function that creates a unique key for each image
def keyer():
    id = uuid.uuid4()
    return str(id)

# Function that creates the metadata object for each image
def datacreator(file,i,size):
    id = keyer()
    patchpath = savepath
    singletonout={
        'name':patchpath.split("/")[-1],
        'id':id,
        'patchpath':patchpath,
        'srcname':file,
        'size':size
    }
    LOCALJSON.append(singletonout)
    
# Function that saves the image
def save_image(image, name):
    #this function is responsible to save the image
    #image is the image to be saved
    #name is the name of the image
    #size is the size of the image
    tf.imsave(name, image)
    namespl = name.split(".")[0]+".jpeg"
    cv2.imwrite(namespl, image)
    
# Function that splits the image
def split_image(impath, size,loc):
    #this function is responsible to split the image into smaller images
    #image is the image to be split
    image = tf.imread(impath)
    reprint(f"Imagesplit has begun")
    numpatches = 0
    for i in range(0, image.shape[0], size):
        for j in range(0, image.shape[1], size):
            if(i+size <= image.shape[0] and j+size <= image.shape[1]):
                cropped = image[i:i+size, j:j+size]
                name = impath.split("/")[-1]
                global savepath
                savepath = f"{loc}/{name[:-4]}-{size}px-{i}-{j}.tif"
                reprint("\e[2K") # clear whole line
                reprint("\e[1G") # move cursor to column 1
                reprint(savepath)
                save_image(cropped, savepath)
                datacreator(name, f'({i},{j})',size)
                numpatches += 1
    print(f"Imagesplit has finished with {numpatches} patches")

# Function that creates the folder structure and calls all the above supporter functions
def main():
    global LOCALJSON
    LOCALJSON = []
    inputter()
    size = [350] #, 512, 3500, 7000]
    for s in size:
        print(f"Carrying out imagesplitting for size = {s}")
        for i in sourcelist:
            global currentimg 
            currentimg = i
            patchpath = os.path.join(f"{out}/{i['newname']}", f'{s//35}x')
            if not os.path.exists(patchpath):
                reprint(f"Folder structure created")
                os.makedirs(patchpath)
            split_image(i['newpath'], s, patchpath)
            metadatawriter(s)
        LOCALJSON.clear()
        print(f"Finished imagesplitting for size = {s}")


main()