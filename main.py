from utils import *
#Path = "C:\\Users\\nblomber\\PycharmProjects\\MetaGen\\testi"
Path = "C:\\Users\\Niko\\PycharmProjects\\MetaGen\\testi"

regex = ','
meta_dict = meta_loader(Path, '.csv')

meta_dict = load_headers(meta_dict, regex)
meta_dict = load_types(meta_dict, regex)

for f in meta_dict.keys():
    print("\nPath: " + f + "\nFilename: " + meta_dict[f].get('filename') + "\nHeaders: ", end="")
    print(meta_dict[f].get('headers'))
    print("Data types: ", end="")
    print(meta_dict[f].get('types'), end="\n")
#meta_save(meta_dict, Path)
