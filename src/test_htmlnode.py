import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag","value","children")
        node2 = HTMLNode("tag","value","children")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = HTMLNode("tag","value","children")
        node2 = HTMLNode("tag2","value","children","props")
        self.assertNotEqual(node,node2)
    def test_props_to_html(self):
        node = HTMLNode("tag","value","children",{"href": "https://www.google.com","target": "_blank"})
        answer = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),answer)
    def test_types_not_eq(self):
        node = print(HTMLNode("tag","value","children","props"))
        answer = 'HTMLNode("tag","value","children","props")'
        self.assertNotEqual(node,answer)
        


if __name__ == "__main__":
    unittest.main()