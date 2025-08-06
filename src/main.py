import os
import shutil
import sys
from generate_pages_recursive import generate_pages_recursive


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_content("./static", "./docs")
    copy_content("./content", "./docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


def copy_content(src, dest, is_root=True):
    abs_src_path = os.path.abspath(src)
    abs_dest_path = os.path.abspath(dest)
    if is_root and os.path.exists(abs_dest_path):
        shutil.rmtree(abs_dest_path)
        os.makedirs(abs_dest_path)
    elif not os.path.exists(abs_dest_path):
        os.makedirs(abs_dest_path)
    if os.path.isdir(abs_src_path):
        for item in os.listdir(abs_src_path):
            new_src = os.path.join(abs_src_path, item)
            new_dest = os.path.join(abs_dest_path, item)
            if os.path.isdir(new_src):
                copy_content(new_src, new_dest, is_root=False)
            else:
                shutil.copy(new_src, new_dest)


main()
