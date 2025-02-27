class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:  # Handles None or an empty dictionary
            return "" 
        string = ""
        for key, value in self.props.items():
            string += f' {key}="{value}"'
        return string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if not self.value:
            raise ValueError("Must have a value")
        if self.tag == None:
            return self.value
        props_html = super().props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def to_html(self):
        if not self.tag:
            raise ValueError("Must have a tag")
        if not self.children:
            raise ValueError("Must have children")
        children_html = []
        for child in self.children:
            child_html = child.to_html()
            children_html.append(child_html)
        all_children_html = "".join(children_html)

        return f"<{self.tag}{self.props_to_html()}>{all_children_html}</{self.tag}>"