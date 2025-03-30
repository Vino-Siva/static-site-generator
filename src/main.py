from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    print(TextNode("This is some anchor text", TextType.LINK,
          "https: // www.boot.dev"))
    print(HTMLNode("<h1></h1>", "This is main heading",
          None, {"href": "https://www.google.com"}))
    HTMLNode.props_to_html(HTMLNode("<h1></h1>", "This is main heading",
                                    None, {"href": "https://www.google.com", "target": "_blank"}))
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())


main()
