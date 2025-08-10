import unittest

from Blocks import *


class TestExtractMarkdownLinksAndImages(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_to_blocks_with_empty_strings(self):
        md = """

        

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_heading_block(self):
        test_func = block_to_block_type("####Umbambe")
        self.assertEqual(test_func,BlockTypes.HEADING_BLOCK)
    def test_code_block(self):
        test_func = block_to_block_type("```bibuppup```")
        self.assertEqual(test_func,BlockTypes.CODE_BLOCK)
    def test_quote_block(self):
        test_func = block_to_block_type(">Tungtungtung\n>sahuur")
        self.assertEqual(test_func,BlockTypes.QUOTE_BLOCK)
    def test_uordered_list(self):
        test_func = block_to_block_type("- Ambambeye\n- kumbba")
        self.assertEqual(test_func,BlockTypes.UNORDERED_LIST)
    def test_ordered_list(self):
        test_func = block_to_block_type("1.  Bilbo\n2. Jabbar")
        self.assertEqual(test_func,BlockTypes.ORDERED_LIST)
    def test_paragraph(self):
        test_func = block_to_block_type("jibobbob tutuppup")
        self.assertEqual(test_func, BlockTypes.PARAGRAPH_BLOCK)
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_heading_with_inline_formatting(self):

        md = "### Heading with **bold** and _italic_"
        html = markdown_to_html_node(md).to_html()
        expected = "<div><h3> Heading with <b>bold</b> and <i>italic</i></h3></div>"
        self.assertEqual(html,expected)
    def test_quote_multiline_with_inline(self):
        md = "> First line\n> Second line with _italic_ text"
        html = markdown_to_html_node(md).to_html()
        expected = "<div><blockquote> First line Second line with <i>italic</i> text</blockquote></div>"
        self.assertEqual(html,expected)
    def test_unordered_list_with_inline_formatting(self):
        md = "- **Bold item**\n- Item with `inline code`"
        html = markdown_to_html_node(md).to_html()
        expected = "<div><ul><li><b>Bold item</b></li><li>Item with <code>inline code</code></li></ul></div>"
        self.assertEqual(html,expected)
    def test_ordered_list_with_inline_formatting(self):
        md = "1. First _italic_\n2. Second with **bold**"
        html = markdown_to_html_node(md).to_html()
        expected = "<div><ol><li>First <i>italic</i></li><li>Second with <b>bold</b></li></ol></div>"
        self.assertEqual(html,expected)
    def test_full_markdown_integration(self):
        md =  """## My **Title**

This is a paragraph with _italic_, **bold**, and `code`.

> Quote line one
> Quote line two

- First list item
- Second list item with **bold**

1. Number one
2. Number two with `code`

```for i in range(3):
    print(i)
```"""
        html = markdown_to_html_node(md).to_html()
        expected =  ("<div>"
        "<h2> My <b>Title</b></h2>"
        "<p>This is a paragraph with <i>italic</i>, <b>bold</b>, and <code>code</code>.</p>"
        "<blockquote> Quote line one Quote line two</blockquote>"
        "<ul><li>First list item</li><li>Second list item with <b>bold</b></li></ul>"
        "<ol><li>Number one</li><li>Number two with <code>code</code></li></ol>"
        "<pre><code>for i in range(3):\n    print(i)\n</code></pre>"
        "</div>")
        self.assertEqual(html,expected)
   
if __name__ == "__main__":
    unittest.main()