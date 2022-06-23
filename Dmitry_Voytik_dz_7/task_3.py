from os import walk, listdir, path
import shutil

name = 'my_project'

try:
    for root, dirs, files in walk(name):
        if 'templates' in dirs and root != name:
            for n in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', n),
                                path.join(name, 'templates', n))
except FileExistsError:
    print('Templates already exist')
except FileNotFoundError:
    print("File(-s) existence error")
