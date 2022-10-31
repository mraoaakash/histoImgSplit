import sys
import os
import pandas as pd


counter = 0
files = [["" for x in range(2)] for y in range(300)]
print(files)

def filelist():
    for file in os.listdir("input"):
        if file.endswith(".tiff"):
            if "HNE" in file.upper():
                print(file)


def mapper():
    return 0
