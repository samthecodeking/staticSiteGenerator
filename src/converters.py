from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text)
        case TextType.BOLD:
            return LeafNode(text_node.text, "b")
        case TextType.ITALIC:
            return LeafNode(text_node.text, "i")
        case TextType.CODE:
            return LeafNode(text_node.text, "code")
        case TextType.LINK:
            return LeafNode(text_node.text, "a", props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("", "img", props={"alt": text_node.text, "src": text_node.url})
        case _:
            raise ValueError("not a valid text type")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:

        #if its not a text node, add it unchanged
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        # Check if the text node contains a delimeter
        if delimiter in old_node.text:
            start_pos = old_node.text.find(delimiter)
            substring_after_first = old_node.text[start_pos + len(delimiter):]
            end_pos_in_substring = substring_after_first.find(delimiter)

            if end_pos_in_substring == -1:
                raise Exception(f"No closing delimeter '{delimiter}' found")
            
            end_pos = start_pos + len(delimiter) + end_pos_in_substring

            # Create 3 new nodes
            before_delimeter = old_node.text[:start_pos]
            between_delimeter = old_node.text[start_pos + len(delimiter):end_pos]
            after_delimeter = old_node.text[end_pos + len(delimiter):]

            # Append the before and inbetween nodes
            if before_delimeter:
                new_nodes.append(TextNode(before_delimeter,TextType.TEXT))
            new_nodes.append(TextNode(between_delimeter, text_type))

            # Recursively process the after part if not empty
            if after_delimeter:
                after_node = TextNode(after_delimeter, TextType.TEXT)
                new_nodes.extend(split_nodes_delimiter([after_node], delimiter, text_type))

        else:
            new_nodes.append(old_node)

    return new_nodes
