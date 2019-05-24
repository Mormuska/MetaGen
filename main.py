from utils import *
""" Meta data generator

Generates csv file that includes names and locations of all files, and headers with header types of targeted files
withing input folder and subfolders bellow it. 
"""

Input_folder = "C:\\Users\\nblomber\\V4InputV4.0.2-UNSW"
name_ext = '.csv'
separator = ','

# Searching for all files
meta_dict = meta_loader(Input_folder)
# Loading headers
meta_dict = load_headers(meta_dict, separator, name_ext)
meta_dict = load_types(meta_dict, separator, name_ext)

# printing to console
# print_on_console(meta_dict)

# Saving to a file
meta_save(meta_dict, "C:\\Users\\nblomber")

selected_list = ["Scenario-Population", "Scenario-Employment", "BaseYearMatrix\\External"]
selected_dict = make_header_list(meta_dict, selected_list, "C:\\Users\\nblomber")
