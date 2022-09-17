import os
from os.path import relpath, join

root_dir = r'my_project2'
dir_dict = {0: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0,10000000: 0}
keys = [0, 100, 1000, 10000, 100000, 1000000, 10000000]
for root, dirs, files in os.walk(root_dir):

    for file in files:
        rel_path = relpath(join(root, file), root_dir)
        size_files = os.stat(join(root_dir, rel_path)).st_size
        if size_files == 0:
            dir_dict[0] += 1
            continue
        try:
            for it, key in enumerate(keys):
                if key < size_files <= keys[it + 1]:
                    dir_dict[keys[it + 1]] += 1
                    break
        except (ValueError, IndexError):
            print(f'IndexError: value is very big for this script')
print(dir_dict)
