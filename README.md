# histoImgSplit

## Introduction
histoImgSplit is an large-format histopathology slide image management pipeline. Most histopathology Machine/ Deep Learning pipelines have the requirement of having large-format images split into patches of various sizes for analysis. This is done for various reasons with the chief reason being ease of creating consistent datasets across a given sample. This pipeline aims to make this process easier.

## What does this pipeline do?
We take the following inputs:
- The path to the original whole-slide-image (WSI)
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
  ..
└── 123-123-123-HnE
    ├── 123-123-123-HnE.tiff
    ├── Patches_125_125
    │   ├── local.json
    │   └── patch_000000_000000
    │       ├── patch_000000_000000.json
    │       └── patch_000000_000000.tiff
    └── master.json
```