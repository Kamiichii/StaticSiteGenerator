import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextType,TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        old_nodes = [TextNode("this is plain**this is bold**plain continues",TextType.PLAIN_TEXT),TextNode("this is just bold",TextType.BOLD_TEXT)]
        nodes = split_nodes_delimiter(old_nodes,"**",TextType.BOLD_TEXT)
        self.assertEqual(nodes,[TextNode("this is plain",TextType.PLAIN_TEXT),TextNode("this is bold",TextType.BOLD_TEXT),TextNode("plain continues",TextType.PLAIN_TEXT),TextNode("this is just bold",TextType.BOLD_TEXT)])
    def test_italic(self):
        old_nodes = [TextNode("this is plain_this is italic_plain continues",TextType.PLAIN_TEXT),TextNode("this is just italic",TextType.ITALIC_TEXT)]
        nodes = split_nodes_delimiter(old_nodes,"_",TextType.ITALIC_TEXT)
        self.assertEqual(nodes,[TextNode("this is plain",TextType.PLAIN_TEXT),TextNode("this is italic",TextType.ITALIC_TEXT),TextNode("plain continues",TextType.PLAIN_TEXT),TextNode("this is just italic",TextType.ITALIC_TEXT)])
    def test_code(self):
        old_nodes = [TextNode("this is plain`this is code`plain continues",TextType.PLAIN_TEXT),TextNode("this is just code",TextType.CODE_TEXT)]
        nodes = split_nodes_delimiter(old_nodes,"`",TextType.CODE_TEXT)
        self.assertEqual(nodes,[TextNode("this is plain",TextType.PLAIN_TEXT),TextNode("this is code",TextType.CODE_TEXT),TextNode("plain continues",TextType.PLAIN_TEXT),TextNode("this is just code",TextType.CODE_TEXT)])
    def test_unclosed_delimiter(self):
        old_nodes = [TextNode("this is a wrong **bold text",TextType.PLAIN_TEXT)]
        with self.assertRaises(Exception):
            nodes = split_nodes_delimiter(old_nodes,"**",TextType.BOLD_TEXT)
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC_TEXT)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
            ],
            new_nodes,
        )
    
    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN_TEXT),
                TextNode("bolded", TextType.BOLD_TEXT),
                TextNode(" word and ", TextType.PLAIN_TEXT),
                TextNode("another", TextType.BOLD_TEXT),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()