import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGES, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
    


if __name__ == "__main__":
    unittest.main()