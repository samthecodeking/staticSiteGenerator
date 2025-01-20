import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equal_nodes(self):
        # Test that two nodes with same content are equal
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("Hello", TextType.TEXT, None)
        self.assertEqual(node1, node2)

    def test_unequal_nodes(self):
        # Test nodes with different content
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("World", TextType.TEXT, None)
        self.assertNotEqual(node1, node2)

    def test_different_types(self):
        # Test nodes with different TextTypes
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("Hello", TextType.BOLD, None)
        self.assertNotEqual(node1, node2)

    def test_different_urls(self):
        # Test nodes with different URLs
        node1 = TextNode("Hello", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Hello", TextType.LINK, "https://google.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()