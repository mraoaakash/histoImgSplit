import openslide
from openslide.deepzoom import DeepZoomGenerator
import numpy as np
import os
import json
from PIL import Image 
import PIL 


image = openslide.OpenSlide("/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/testImage/20190610_541_528-18_1412-18-A_Biopsy_TNBC_HnE_40X.tif")
# image = openslide.OpenSlide("/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/testImage/20190610_541_528-18_1412-18-A_Biopsy_TNBC_HnE_40X.tif")
# print(image.dimensions)
tile_size =[256,512,1024]
for p in range(len(tile_size)):
    x = tile_size[p]
    dzoomImg = DeepZoomGenerator(image, tile_size=x, overlap=1, limit_bounds=True)
    # print(dzoomImg.level_count)
    # print(dzoomImg.level_tiles)
    print(dzoomImg.level_dimensions)
    for i in range(dzoomImg.level_count):    
        # deepzwsi = dzoomImg.get_tile(i, address = (0, 0))
        # print(deepzwsi)
        leveltiles = dzoomImg.level_tiles[i]
        print(f'leveltiles_{i} : {leveltiles}')
        for j in range(0,leveltiles[0]):
            for k in range(0,leveltiles[1]):
                deepzwsi = dzoomImg.get_tile(i, address = (j, k))
                if not os.path.isdir(f"/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/OpenSlideGen/{x}/level{str(i)}"):
                        os.makedirs(f"/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/OpenSlideGen/{x}/level{str(i)}")
                im1 = deepzwsi.save(f"/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/OpenSlideGen/{x}/level{str(i)}/downsampWSI_level{str(i)}_{str(j)}_{str(k)}.jpg")
                # if not os.path.isdir(f"/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/OpenSlideGen/{x}/level{str(i)}"):
                #         os.makedirs(f"/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/OpenSlideGen/{x}/level{str(i)}")
                # im1 = deepzwsi.save(f"/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/OpenSlideGen/{x}/level{str(i)}/downsampWSI_level{str(i)}_{str(j)}_{str(k)}.jpg")

