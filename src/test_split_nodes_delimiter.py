import unittest

from split_nodes_delimiter import split_nodes_delimiter,split_nodes_image,split_nodes_link
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
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.IMAGE_TEXT, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )
    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE_TEXT, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [to habibland](https://habibland.com) and another [to bambakamba](https://i.elelolabamba.com)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("to habibland", TextType.LINK_TEXT, "https://habibland.com"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "to bambakamba", TextType.LINK_TEXT, "https://i.elelolabamba.com"
                ),
            ],
            new_nodes,
        )

    
if __name__ == "__main__":
    unittest.main()