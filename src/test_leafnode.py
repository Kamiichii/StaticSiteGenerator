import unittest

from LeafNode import LeafNode

class TestLeafNode(unittest.TestCase):
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