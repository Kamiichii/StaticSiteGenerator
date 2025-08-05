import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode


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
    
class TestLeafNode(unittest.TestCase):    
    def test_leaf_to_html_p(self):
     node = LeafNode("p", "Hello, world!")
     self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
     node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
     self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
   
   def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

   def test_to_html_with_multiple_children(self):
    child_node = LeafNode("span", "child")
    child_node2= LeafNode("a","heyo")
    parent_node = ParentNode("div", [child_node,child_node2])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span><a>heyo</a></div>")
    
   def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

   def test_to_html_with_no_children(self):
    parent_node = ParentNode("div",None)
    self.assertRaises(ValueError)
    
    


if __name__ == "__main__":
    unittest.main()