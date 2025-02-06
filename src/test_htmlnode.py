import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_single_child(self):
        node = ParentNode("div", [LeafNode("Hello")])
        self.assertEqual(node.to_html(), '<div>Hello</div>')

    def test_multi_child(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i")
            ],
            {"class": "greeting"}
        )
        self.assertEqual(parent.to_html(), '<p class="greeting"><b>Bold text</b>Normal text<i>italic text</i></p>')

    def test_nested_child(self):
        nested = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode("Hello")])
            ]
        )
        self.assertEqual(nested.to_html(), '<div><p>Hello</p></div>')

    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("Hello")])
            node.to_html()

    def test_empty_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", [])
            node.to_html()
    
    def test_None_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", children=None)
            node.to_html()

if __name__ == "__main__":
    unittest.main()