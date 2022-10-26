# histoImgSplit

## Introduction
histoImgSplit is an large-format histopathology slide image management pipeline. Most histopathology Machine/ Deep Learning pipelines have the requirement of having large-format images split into patches of various sizes for analysis. This is done for various reasons with the chief reason being ease of creating consistent datasets across a given sample. This pipeline aims to make this process easier.

## What does this pipeline do?
We take the following inputs:
- The path to the original whole-slide-image (WSI)
- The output location where the results must be stored
- The output image size (based on the level of zoom at which the patches are generated)

We output the following:
- A master folder with,
    - A specific folder for a given image with,
        - The original image
        - The patches based on selected zoom levels
        - A local json with
            - Patch name
            - Patch md5-sum
            - Patch path
            - Patch 
    - A master json with,
        - Paths to all files
        - Unique IDs of each file
        - MD5-sum generated for a given file