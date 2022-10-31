import shutil # for copying files
import os # for checking if file exists
import numpy as np # for image processing
import fnmatch # for matching file names
import uuid





def imgRet(key='hne'):
    exclude = list(((open("/home/aakash.rao_ug23/cloud/histoImgSplit/illfold.txt","r")).read().strip()).split(",")) 
    # list of folders to exclude
    # Removed exclusion rules from here to ensure data privacy
    for subdir, dirs, files in os.walk("/storage/tnbc"):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if fnmatch.fnmatch(file, '*.tif'):
                if key in file.lower() and (("cropped" in file.lower())==False):
                    prpath=str(os.path.join(subdir, file))
                    print(file)
                    id = uuid.uuid4()
                    print(id)
                    # if os.path.isfile(os.path.join("/storage/tnbc/NewDatasetHnE/work_copy", file)) == False:
                    #     print(f"")
                        # shutil.copy(prpath, "/storage/tnbc/NewDatasetHnE/work_copy")
					#call yout preferred function here
					#can be	randcrop or imgcrop or any
					#custom function

imgRet()