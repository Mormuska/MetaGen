import os, ast


def meta_loader(absolute_path, name_ext):
    """
    Finds all files with name_ext (e.q '.csv') in the chosen input folder and subfolders under it. Loads headers from
    the file and saves them, filename and file location into a meta_dict dictionary where file location is the KEY.

    :param absolute_path: Absolute path to input  (String)
    :param name_ext: Filename extension (String)
    :return meta_dict: Metadata stored in a dictionary. PATH to a file is the KEY and it includes HEADERS and FILENAME
    """
    meta_dict = {}
    for root, dirs, files in os.walk(absolute_path):
        for f in files:
            if name_ext in f:
                meta_dict[os.path.join(root, f)] = {'filename': f}
    return meta_dict


def load_headers(meta_dict, regex):

    for path in meta_dict:
        file_obj = open(path, 'r')
        headers = file_obj.readline().rstrip().split(regex)
        meta_dict[path].update({'headers': headers})
        file_obj.close()
    return meta_dict


def load_types(meta_dict, regex):

    for path in meta_dict:
        types = []
        file_obj = open(path, 'r')
        next(file_obj)   # Skipping headers
        first_line = file_obj.readline().rstrip().split(regex)
        for member in first_line:
            try:
                types.append(type(ast.literal_eval(member)).__name__)
            except ValueError:
                types.append("Unknown")
                # Prompt Logger
        meta_dict[path].update({'types': types})
        file_obj.close()
    return meta_dict

#
# def meta_save(meta_dict, absolute_path, name="\Meta_data.csv", append=False):
#     path = absolute_path + name
#     if append:
#         file_obj = open(path, 'a')
#     else:
#         file_obj = open(path, 'w')
#     file_obj.write('asd;absolute_path')
#
#     file_obj.close()
#     print("Metadata saved into %s", path)
#     return
