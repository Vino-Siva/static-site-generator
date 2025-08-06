import os
import re
from block_markdown import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()
    node = markdown_to_html_node(md_content)
    html = node.to_html()
    title = extract_title(md_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    if basepath != "/" and not basepath.endswith("/"):
        basepath += "/"
    template_content = re.sub(r'href=(["\'])/', rf"href=\1{basepath}", template_content)
    template_content = re.sub(r'src=(["\'])/', rf"src=\1{basepath}", template_content)
    abs_dest_path = os.path.abspath(dest_path)
    new_dir_path = os.path.dirname(abs_dest_path)
    new_abs_path = os.path.abspath(new_dir_path)
    os.makedirs(new_abs_path, exist_ok=True)
    with open(abs_dest_path, "w") as f:
        f.write(template_content)
