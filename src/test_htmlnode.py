import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_multiple_props(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_single_props(self):
        node = HTMLNode(props={"id":"main-content"})

if __name__ == "__main__":
    unittest.main()