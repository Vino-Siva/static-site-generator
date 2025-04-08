class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        new_string = ""
        for prop in self.props.items():
            new_string += f' {prop[0]}="{prop[1]}"'
        return new_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leafnode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parentnode must have a children")
        if self.children is None:
            raise ValueError("child element is missing")
        new_children = self.children
        new_child_element = ""
        for child in new_children:
            if isinstance(child, LeafNode):
                new_child_element += child.to_html()
            if isinstance(child, ParentNode):
                new_child_element += f"{child.to_html()}"

        return f"<{self.tag}{self.props_to_html()}>{new_child_element}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
