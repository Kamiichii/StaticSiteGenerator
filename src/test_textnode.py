import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_text_different(self):
        node = TextNode("different text test 1", TextType.BOLD)
        node2 = TextNode("different text test 2", TextType.BOLD)
        self.assertNotEqual(node,node2)
    def test_textType_different(self):
        node = TextNode("Different texttype test", TextType.BOLD)
        node2 = TextNode("Different texttype test", TextType.ITALIC)
        self.assertNotEqual(node,node2)
    def test_url_different(self):
        node = TextNode("url different", TextType.BOLD, "https...")
        node2 = TextNode("url different", TextType.BOLD, "https...")
        self.assertEqual(node,node2)
    


if __name__ == "__main__":
    unittest.main()