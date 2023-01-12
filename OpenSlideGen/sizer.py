import os
import cv2

def get_size(image_path, level):
    filepath = f'{image_path}/L{level}'
    length = 0
    width = 0
    for item in os.listdir(filepath):
        meta = item.split('_')
        meta[-1] = meta[-1].split('.')[0]
        # print(meta[0], meta[1], meta[2])
        img = cv2.imread(f'{filepath}/{item}')
        # print(img.shape[0], img.shape[1])
        if meta[1] == '1':
            length += img.shape[0]
        if meta[2] == '0':
            width += img.shape[1]
        
    print(f'Length: {length}, Width: {width}')



if __name__ == "__main__":
    path = "/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/OpenSlideGen/images"
    for i in range(9,18):
        get_size(path, i)