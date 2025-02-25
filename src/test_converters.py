import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from converters import text_node_to_html_node

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

    def test_test(self):
        textnode = TextNode("Testing 123", TextType.TEXT)
        result = text_node_to_html_node(textnode)
        self.assertEqual(result.value, "Testing 123")
        self.assertEqual(result.tag, None)

    def test_wrong_type(self):
        textnode = TextNode("Testing 123", 999)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(textnode)
        self.assertEqual(str(context.exception), "not a valid text type")


