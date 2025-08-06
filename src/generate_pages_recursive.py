import os
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isdir(dir_path_content):
        src_dir_list = os.listdir(dir_path_content)
        for item in src_dir_list:
            item_path = os.path.join(dir_path_content, item)
            abs_dest_path = os.path.abspath(dest_dir_path)
            if os.path.isfile(item_path) and item.endswith(".md"):
                name, ext = os.path.splitext(item)
                dest_path = os.path.join(abs_dest_path, name + ".html")
                generate_page(item_path, template_path, dest_path, basepath)
            elif os.path.isdir(item_path):
                new_dest_path = os.path.join(dest_dir_path, item)
                check_abs_dest_path = os.path.abspath(new_dest_path)
                if not os.path.exists(check_abs_dest_path):
                    os.makedirs(check_abs_dest_path)
                generate_pages_recursive(
                    item_path, template_path, new_dest_path, basepath
                )
