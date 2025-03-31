from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []
    delimiters = ["**", "_", "`"]
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_node.append(node)
            continue
        if node.text.count(delimiter) % 2 > 0:
            raise Exception(f"invalid Markdown syntax: {node.text}")
        if delimiter not in delimiters:
            raise Exception(f"invalid delimiter provided: {delimiter}")
        split_text = node.text.split(delimiter)
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                new_node.append(TextNode(split_text[i], node.text_type))
            else:
                new_node.append(TextNode(split_text[i], text_type))

    return new_node


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
