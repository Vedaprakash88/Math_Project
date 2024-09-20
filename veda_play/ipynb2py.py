import json
import os
import easygui

root = easygui.diropenbox(msg="Select folder with ipynb files", title="IPYNB to PY converter")
counter = 0
converted = 0
skipped = 0
for path, subdirs, files in os.walk(root):
    for file in files:
        name, ext = os.path.splitext(file)
        if ext == ".ipynb":
            counter += 1
            try:
                f_path = os.path.join(path, file)
                code = json.load(open(f_path))
                py_file = open(f"{f_path}.py", "w+")
                for cell in code['cells']:
                    if cell['cell_type'] == 'code':
                        for line in cell['source']:
                            py_file.write(line)
                        py_file.write("\n")
                    elif cell['cell_type'] == 'markdown':
                        py_file.write("\n")
                        for line in cell['source']:
                            if line and line[0] == "#":
                                py_file.write(line)
                        py_file.write("\n")
                py_file.close()
                converted += 1
                os.remove(f_path)
            except Exception as e:
                print(f'Could not process "{f_path}" file due to following error: [{e}]')
                skipped += 0
print(f"{counter} ipynb file found, {converted} files converted, {skipped} files skipped")