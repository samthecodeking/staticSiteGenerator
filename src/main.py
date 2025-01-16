from textnode import TextNode, TextType

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

if __name__ == "__main__":
    main()