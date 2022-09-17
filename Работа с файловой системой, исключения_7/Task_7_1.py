import os
dir_name = 'my_project1'
path = ['settings', 'mainapp', 'adminapp', 'authapp']
for i in path:
    dir_path = os.path.join(dir_name, i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

