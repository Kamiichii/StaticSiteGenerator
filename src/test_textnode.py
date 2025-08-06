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
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_text_bold(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    def test_text_link(self):
        node = TextNode("This is a text node", TextType.LINK_TEXT,"Insert rickroll url here")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props,{"href":"Insert rickroll url here"})
    def test_text_image(self):
        node = TextNode("This is an anchor text", TextType.IMAGE_TEXT,"Insert rickroll url here")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props,{"src":"Insert rickroll url here","alt":"This is an anchor text"}) 



if __name__ == "__main__":
    unittest.main()