import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from converters import text_node_to_html_node

class TestTextToHTML(unittest.TestCase):
    def test_bold(self):
        textnode = TextNode("Testing 123", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(textnode), LeafNode("b", "Testing 123", None))