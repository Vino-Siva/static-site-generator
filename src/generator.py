import os
import shutil


# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# shutil.copy
# shutil.rmtree
def copier(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    new_path = os.listdir(source)
    new_dir = os.mkdir("../public")
    os.path.join(new_dir, new_path)

    pass
