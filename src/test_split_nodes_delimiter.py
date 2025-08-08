import unittest

from split_nodes_delimiter import split_nodes_delimiter,split_nodes_image,split_nodes_link,text_to_textnodes
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
    def test_text_to_textnodes_complete_example(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.PLAIN_TEXT),
            TextNode("obi wan image", TextType.IMAGE_TEXT, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK_TEXT, "https://boot.dev"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_text_to_textnodes_plain_text_only(self):
        text = "This is just plain text"
        expected = [TextNode("This is just plain text", TextType.PLAIN_TEXT)]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_text_to_textnodes_bold_only(self):
        text = "This has **bold** text"
        expected = [
            TextNode("This has ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.PLAIN_TEXT),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_text_to_textnodes_multiple_formats(self):
        text = "**Bold** and _italic_ and `code`"
        expected = [
            TextNode("Bold", TextType.BOLD_TEXT),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("code", TextType.CODE_TEXT),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)
    
if __name__ == "__main__":
    unittest.main()