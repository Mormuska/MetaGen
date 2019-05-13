from utils import *
Path = "C:\\Users\\nblomber\\PycharmProjects\\MetaGen\\testi"


meta_dict = meta_loader(Path, '.csv')

meta_dict = load_headers(meta_dict)
meta_dict = load_types(meta_dict)

for f in meta_dict.keys():
    print("\nPath: " + f + "\nFilename: " + meta_dict[f].get('filename') + "\nHeaders: ", end="")
    print(meta_dict[f].get('headers'))
    print("Data types: ", end="")
    print(meta_dict[f].get('types'), end="\n")
