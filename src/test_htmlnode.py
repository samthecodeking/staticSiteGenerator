import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_multiple_props(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_single_props(self):
        node = HTMLNode(props={"id":"main-content"})
        self.assertEqual(node.props_to_html(), ' id="main-content"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_node_multiprop(self):
        node = LeafNode("Hello", "p", props={"class": "highlight", "href": "https://example.com"})
        self.assertEqual(node.to_html(), '<p class="highlight" href="https://example.com">Hello</p>')

    def test_leaf_node_missing_value(self):
        node = LeafNode(value=None, tag = "p")
        with self.assertRaises(ValueError) as context:  # Expect a ValueError
            node.to_html()
        self.assertEqual(str(context.exception), "Must have a value")  # Check the error message

    def test_leaf_node_missing_value_and_tag(self):
        node = LeafNode(value="", tag = None)
        with self.assertRaises(ValueError) as context:  # Expect a ValueError
            node.to_html()
        self.assertEqual(str(context.exception), "Must have a value")  # Check the error message
    
    def test_leaf_node_empty_value_and__missing_tag(self):
        node = LeafNode(value=None, tag = None)
        with self.assertRaises(ValueError) as context:  # Expect a ValueError
            node.to_html()
        self.assertEqual(str(context.exception), "Must have a value")  # Check the error message
    
    def test_leaf_node_missing_tag(self):
        node = LeafNode("Hello", None, props={"class": "highlight", "href": "https://example.com"})
        output = node.to_html()
        self.assertEqual(output, 'Hello')


if __name__ == "__main__":
    unittest.main()