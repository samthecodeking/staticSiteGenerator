import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from converters import text_node_to_html_node, split_nodes_delimiter

class TestTextToHTML(unittest.TestCase):
    def test_bold(self):
        textnode = TextNode("Testing 123", TextType.BOLD)
        result = text_node_to_html_node(textnode)
        self.assertEqual(result.value, "Testing 123")
        self.assertEqual(result.tag, "b")

    def test_italic(self):
        textnode = TextNode("Testing 123", TextType.ITALIC)
        result = text_node_to_html_node(textnode)
        self.assertEqual(result.value, "Testing 123")
        self.assertEqual(result.tag, "i")

    def test_code(self):
        textnode = TextNode("Testing 123", TextType.CODE)
        result = text_node_to_html_node(textnode)
        self.assertEqual(result.value, "Testing 123")
        self.assertEqual(result.tag, "code")

    def test_text(self):
        textnode = TextNode("Testing 123", TextType.TEXT)
        result = text_node_to_html_node(textnode)
        self.assertEqual(result.value, "Testing 123")
        self.assertEqual(result.tag, None)

    def test_wrong_type(self):
        textnode = TextNode("Testing 123", 999)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(textnode)
        self.assertEqual(str(context.exception), "not a valid text type")

    def test_link(self):
        textnode = TextNode("Testing 123", TextType.LINK, "https://www.boot.dev")
        result = text_node_to_html_node(textnode)
        self.assertEqual(result.value, "Testing 123")
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.props, {"href": "https://www.boot.dev"})

    def test_image(self):
        textnode = TextNode("Testing 123", TextType.IMAGE, "https://www.boot.dev/logo.png")
        result = text_node_to_html_node(textnode)
        self.assertEqual(result.value, "")
        self.assertEqual(result.tag, "img")
        self.assertEqual(result.props, {"alt": "Testing 123" ,"src": "https://www.boot.dev/logo.png"})

class TestSplitNodesDelimiter(unittest.TestCase):
    def setUp(self):
        self.text_type_bold = TextType.BOLD  # Example text type for testing
    
    def test_no_delimiter(self):
        old_nodes = [TextNode("Hello world", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "**", self.text_type_bold)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Hello world")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_single_delimiter_pair(self):
        old_nodes = [TextNode("Hello **bold** world", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "**", self.text_type_bold)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, self.text_type_bold)
        self.assertEqual(result[2].text, " world")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_multiple_delimiters(self):
        old_nodes = [TextNode("This **is** a **test**", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "**", self.text_type_bold)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "This ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "is")
        self.assertEqual(result[1].text_type, self.text_type_bold)
        self.assertEqual(result[2].text, " a ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "test")
        self.assertEqual(result[3].text_type, self.text_type_bold)

    def test_missing_closing_delimiter(self):
        old_nodes = [TextNode("Hello **world", TextType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_nodes, "**", self.text_type_bold)
        self.assertTrue("No closing delimeter" in str(context.exception))

    def test_non_text_nodes(self):
        old_nodes = [TextNode("Hello", TextType.TEXT), TextNode("Image", TextType.IMAGE)]
        result = split_nodes_delimiter(old_nodes, "**", self.text_type_bold)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.IMAGE)