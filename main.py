from utils import *
Path = "D:\\Data\\V4InputV4.0.2-UNSW"

name_ext = '.csv'
regex = ','
meta_dict = meta_loader(Path)

meta_dict = load_headers(meta_dict, regex, name_ext)
meta_dict = load_types(meta_dict, regex, name_ext)

for f in meta_dict.keys():
    print("\nPath: " + f + "\nFilename: " + meta_dict[f].get('filename') + "\nHeaders: ", end="")
    print(meta_dict[f].get('headers'))
    print("Data types: ", end="")
    print(meta_dict[f].get('types'), end="\n")
print(len(meta_dict.keys()))
meta_save(meta_dict, "D:\\Data")
