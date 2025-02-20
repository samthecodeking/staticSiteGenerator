from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from converters import text_node_to_html_node

def main():

    # Create a basic text node
    text_node = TextNode("Hello world", TextType.TEXT)
    print(f"text_node = {text_node}")

    # Or a bold text node
    bold_node = TextNode("Important text", TextType.BOLD)
    print(f"bold_node = {bold_node}")

    # Or a link node
    link_node = TextNode("Click here", TextType.LINK, "https://www.boot.dev")
    print(f"link_node = {link_node}") 


    # html node test
    html_node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
    print(f"html_node = {html_node}")

    # Leaf node test
    leaf_node = LeafNode("Hello", "p", props={"class": "highlight"})
    html_leaf_node = leaf_node.to_html()
    print(f"leaf_node = {leaf_node}")
    print(f"html_leaf_node = {html_leaf_node}")

    leaf_node2 = LeafNode("Hello", "p", props={"class": "highlight", "href": "https://example.com"})
    html_leaf_node2= leaf_node2.to_html()
    print(f"leaf_node2 = {leaf_node2}")
    print(f"html_leaf_node2 = {html_leaf_node2}")

    # Parent Node test
    parent_node = ParentNode("p",children=[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text")])
    print(f"parent_node = {parent_node}")
    parent_node2 = ParentNode("div", [LeafNode("Hello")])
    print(f"parent_node2 = {parent_node2} - HTML = {parent_node2.to_html()}")
    
    parent_node3 = ParentNode(
        "p",
        [
            LeafNode("Bold text", "b"),
             LeafNode("Normal text"),
            LeafNode("italic text", "i")
        ],
        {"class": "greeting"}
    )
    print(f"parent_node3 = {parent_node3} - HTML = {parent_node3.to_html()}")

    nested = ParentNode(
        "div",
        [
                ParentNode("p", [LeafNode("Hello")])
        ]
    )
    print(f"nested = {nested} - HTML = {nested.to_html()}")

    #convert text to html test
    textnode = TextNode("Testing 123", TextType.BOLD)
    print(f"textnode = {textnode}")
    print(f"Converted = {text_node_to_html_node(textnode)}")


if __name__ == "__main__":
    main()