import openslide
from openslide.deepzoom import DeepZoomGenerator
import numpy as np
import os
import json
from PIL import Image 
import PIL 


image = openslide.OpenSlide("/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/testImage/20190610_541_528-18_1412-18-A_Biopsy_TNBC_HnE_40X.tif")
# print(image.dimensions)
tile_size =1024
dzoomImg = DeepZoomGenerator(image, tile_size=tile_size, overlap=1, limit_bounds=False)
# print(dzoomImg.level_count)
# print(dzoomImg.level_tiles)
print(dzoomImg.level_dimensions)
for i in range(dzoomImg.level_count):    
    deepzwsi = dzoomImg.get_tile(i, address = (0, 0))
    # print(deepzwsi)
    leveltiles = dzoomImg.level_tiles[i]
    print(f'leveltiles_{i} : {leveltiles}')
    for j in range(0,leveltiles[0]):
        for k in range(0,leveltiles[1]):
            deepzwsi = dzoomImg.get_tile(i, address = (j, k))
            if deepzwsi.size[0] == deepzwsi.size[1]:
                if deepzwsi.size[0] >= tile_size:
                    deepzwsi = deepzwsi.resize((512,512)) 
            if not os.path.isdir(f"/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/downsampler/level{str(i)}"):
                    os.makedirs(f"/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/downsampler/level{str(i)}")
            im1 = deepzwsi.save(f"/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/downsampler/level{str(i)}/downsampWSI_level{str(i)}_{str(j)}_{str(k)}.jpg")
