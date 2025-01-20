import unittest

from HTMLNode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    def test_dif_tag(self):
        node = HTMLNode("test_tag", None , None , None)
        node2 = HTMLNode("test_tag2", None , None , None)
        self.assertNotEqual(node,node2)
    def test_dif_props(self):
        node = HTMLNode(None,None,None,{"test_key": "test_value"})
        node2 = HTMLNode(None,None,None,{"test_key2":"test_value2"})
        self.assertNotEqual(node,node2)
    def test_repr(self):
        node = HTMLNode("test_tag","test_value","test_childeren",{"test_key": "test_value"})
        self.assertEqual(node.__repr__(), "HTMLNode(test_tag,test_value,test_childeren,{'test_key': 'test_value'})")



if __name__ == "__main__":
    unittest.main()