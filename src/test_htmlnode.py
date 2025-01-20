import unittest

from HTMLNode import HTMLNode,LeafNode

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
    def test_value_is_dif(self):
        node = LeafNode(None,"this is a value")
        node2 = LeafNode(None, "this is a value2")
        self.assertNotEqual(node,node2)
    def test_tag_is_dif(self):
        node = LeafNode("this is a tag",None)
        node2 = LeafNode("this is a tag 2", None)
        self.assertNotEqual(node,node2)
    def test_tohtml_is_working(self):
        node = LeafNode("tag","value",{"href":"ibibik"})
        if node.to_html() == f'<tag href="ibibik">value</tag>':
            return True
        else:
            return False
    



if __name__ == "__main__":
    unittest.main()