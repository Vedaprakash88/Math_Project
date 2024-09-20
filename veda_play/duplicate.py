import os
import pandas as pd
from collections import defaultdict


def get_files_in_dir(directory):
    files_dict = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            size = os.path.getsize(os.path.join(dirpath, filename))
            files_dict[filename].append(os.path.join(dirpath, filename))
            files_dict[filename].append(size)
    return files_dict


path = "D:\\9. MEDIA\\Photos\\"
files_dict = get_files_in_dir(path)
excel_file_path = os.path.join(path, "filenames.xlsx")
df_filenames = pd.DataFrame.from_dict(files_dict,  orient='index')
list_index = df_filenames.index.has_duplicates
df_filenames.to_excel(excel_file_path, index=True, header=True)
