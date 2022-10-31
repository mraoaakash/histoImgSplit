import shutil # for copying files
import os # for checking if file exists
import numpy as np # for image processing
import fnmatch # for matching file names
import 




def imgRet(key='hne'):
    exclude = list(((open("MyFile.txt","a")).read()).split(",")) # list of files to exclude
    print(exclude)
    for subdir, dirs, files in os.walk("/storage/tnbc"):
        print(dirs)
        print(subdir)
        print(files)
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if fnmatch.fnmatch(file, '*.tif'):
                if key in file.lower() and (("cropped" in file.lower())==False):
                    prpath=str(os.path.join(subdir, file))
                    # print(file)
                    # if os.path.isfile(os.path.join("/storage/tnbc/NewDatasetHnE/work_copy", file)) == False:
                    #     print(f"")
                        # shutil.copy(prpath, "/storage/tnbc/NewDatasetHnE/work_copy")
					#call yout preferred function here
					#can be	randcrop or imgcrop or any
					#custom function

imgRet()