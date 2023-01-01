import PIL
from PIL import Image
from PIL import ImageFilter
import os

outpath = "/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/upsampler/out"
inpath = "/Users/mraoaakash/Documents/research/research-tnbc/histoImgSplit/upsampler/input"

def interpolator(path, scale=10):
    img = Image.open(path)
    name= path.split('/')[-1]
    bilinear_img = img.resize((1000,1000), PIL.Image.BILINEAR )
    bilinear_img.save(os.path.join(outpath,name))
    sharpened1 = bilinear_img.filter(ImageFilter.SHARPEN);
    sharpened2 = sharpened1.filter(ImageFilter.SHARPEN);

    # Show the sharpened images
    sharpened1.save(os.path.join(outpath,f'sharpened1_{name}'))
    sharpened2.save(os.path.join(outpath,f'sharpened2_{name}'))

def main():
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    for i in os.listdir(inpath):
        interpolator(os.path.join(inpath,i))

main()