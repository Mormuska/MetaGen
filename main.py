import os
Path = "C:\\Users\\nblomber\\PycharmProjects\\MetaGen\\testi"

dict = {}
headers = "asd7;asd2:asd89"

for root, dirs, files in os.walk(Path):
    for f in files:
        if '.csv' in f:
            dict[os.path.join(root, f)] = {'filename': f, 'headers': headers}

for f in dict.keys():
    print("Path: " + f + "\nFilename: " + dict[f].get('filename') + "\nHeaders: " + dict[f].get('headers'))

# import os

# for file in os.listdir(Path):
#     if file.endswith(".csv"):
#         print(os.path.join(Path, file))
#

# GLOB
# import glob
# Path = "C:\\Users\\nblomber\\PycharmProjects\\MetaGen\\testi"
#
#
# files = [f for f in glob.glob(Path, recursive=True)]
# print(files)
