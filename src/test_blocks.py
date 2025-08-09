import unittest

from Blocks import markdown_to_blocks,block_to_block_type,BlockTypes


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


if __name__ == "__main__":
    unittest.main()