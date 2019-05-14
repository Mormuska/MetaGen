from utils import *
""" Meta data generator

Generates csv file that includes names and locations of all files, and headers with header types of targeted files
withing input folder and subfolders bellow it. 
"""

Input_folder = "C:\\Users\\nblomber\\V4InputV4.0.2-UNSW"
name_ext = '.csv'
regex = ','

# Searching for all files
meta_dict = meta_loader(Input_folder)
# Loading headers
meta_dict = load_headers(meta_dict, regex, name_ext)
meta_dict = load_types(meta_dict, regex, name_ext)

# printing to console
for f in meta_dict.keys():
    print("\nPath: " + f + "\nFilename: " + meta_dict[f].get('filename') + "\nHeaders: ", end="")
    print(meta_dict[f].get('headers'))
    print("Data types: ", end="")
    print(meta_dict[f].get('types'), end="\n")
print(len(meta_dict.keys()))

# Saving to a file
meta_save(meta_dict, "D:\\Data")

