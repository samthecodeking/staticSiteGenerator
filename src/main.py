from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

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

if __name__ == "__main__":
    main()