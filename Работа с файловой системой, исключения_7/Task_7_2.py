import os
import shutil

root_dir = os.path.join(os.path.dirname(__file__), 'my_project')
dirs_files = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(dirs_files):
    os.makedirs(dirs_files)

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for element in dirs:
            if not os.path.exists(os.path.join(dirs_files, element)):
                os.makedirs(os.path.join(dirs_files, element))

        for file in files:
            root_file = os.path.join(root, file)
            dir_file = os.path.join(dirs_files, os.path.basename(root))
            if not os.path.dirname(root_file) == dir_file:
                shutil.copy(root_file, dir_file)
