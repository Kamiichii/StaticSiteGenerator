import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_texts_not_eq(self):
        node = TextNode("Text1",TextType.PLAIN_TEXT,None)
        node2 = TextNode("Text2",TextType.PLAIN_TEXT,None)
        self.assertNotEqual(node,node2)
    def test_url_not_none(self):
        node = TextNode("Text",TextType.IMAGE_TEXT,"testurl")
        node2 = TextNode("Text",TextType.IMAGE_TEXT,"testurl")
        self.assertEqual(node,node2)
    def test_types_not_eq(self):
        node = TextNode("Text",TextType.ITALIC_TEXT,None)
        node2 = TextNode("Text",TextType.PLAIN_TEXT,None)
        self.assertNotEqual(node,node2)
        


if __name__ == "__main__":
    unittest.main()