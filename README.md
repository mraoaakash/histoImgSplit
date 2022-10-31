# histoImgSplit
This codebase is a part of a larger codebase for the study of Triple Negative Breast Cancer at Ashoka University's Centre for Health Analytics and Trends (CHART).

## Introduction
histoImgSplit is an large-format histopathology slide image management pipeline. Most histopathology Machine/ Deep Learning pipelines have the requirement of having large-format images split into patches of various sizes for analysis. This is done for various reasons with the chief reason being ease of creating consistent datasets across a given sample. This pipeline aims to make this process easier.

## Function of the pipeline:
The given pipeline takes in a whole-slide-image (WSI) image path, an output path and a few other parameters, and outputs a structured set of patches based on the input parameters. The pipeline works exclusively on tiff files as they are the standard for storing large format images. This pipeline also creates metadata for the different patches generated as well as the WSI.

This pipeline also deals with the organization of the images into a structured manner. The larger project that this pipeline is being designed for, involves various other functions, requiring mutliple file structures. We have narrowed this down to three distinct structures. 
1. A master copy of the images obtained from the lab
2. A working copy that is name-mapped to our internal naming convention (convention mentioned ahead) with a mapping back to the original WSI.
3. A list of all the patches named with UUIDs, with a list of mappings back to the original WSI


The WSIs used here are HnE stained breast cancer histopathology images obtained from various sources. The naming convention followed here would be:
```
S01-AU-000000-R.tiff
```
where, ```S01``` indicates the site the sample is collected from, ```AU``` marks Ashoka University, ```000000``` six digit image ID, and ```R``` to denote that the image is the Raw unedited WSI, all separated by a ```-```.

The Patches derived from a given WSI will have the following naming convention:
```
S01-AU-000000-R-x-y.tiff
```
where, the first 15 digits are the same as the WSI to ensure easy mapping back to the WSI, followed by the top-left coordinate that the image is derived from, represented above by ```x-y``` (6 digit numbers with leading 0s). 

## I/O:
We take the following inputs:
- The path to the original WSI
- The output location where the results must be stored
- The output image size (based on the level of zoom at which the patches are generated)
- The overlap setting used (0 by default)

We output the following:
- A master folder with,
    - A specific folder for a given image with,
        - The original image
        - A folder for a given size with patches based on selected zoom level with,
            - A local json with,
                - Patch name
                - Patch md5-sum
                - Patch path
                - Patch coordinates (top left x,y)
                - Overlap setting (0 by default)
    - A master json with,
        - Paths to all files
        - MD5-sum generated for a given file

Example, for a given WSI "123-123-123-HnE.tiff" we have the file tree as follows:

```
.
└── 123-123-123-HnE
    ├── 123-123-123-HnE.tiff
    ├── Patches_125_125
    │   ├── local.json
    │   ├── patch_000000_000000
    │   │   ├── patch_000000_000000.json
    │   │   └── patch_000000_000000.tiff
    │   ├── patch_000125_000000
    │   │   ├── patch_000125_000000.json
    │   │   └── patch_000125_000000.tiff
    │   ├── patch_000250_000000
    │   │   ├── patch_000250_000000.json
    │   │   └── patch_000250_000000.tiff
    │   ├── patch_000375_000000
    │   │   ├── patch_000375_000000.json
    │   │   └── patch_000375_000000.tiff
    │   └── patch_000500_000000
    │       ├── patch_000500_000000.json
    │       └── patch_000500_000000.tiff
    └── master.json
```

(Here, we assume the input file path is provided as well as the output file path and our patch size is decided at 125x125 pixels, with the overlap set to the default value of 0. Additionally we are only showing the first 5 patches generated for the sake of simplicity.)