import unittest

from extract_markdown_links_and_images import ExtractMarkdownLinksAndImages


class TestExtractMarkdownLinksAndImages(unittest.TestCase):
    def test_extract_markdown_images(self):
      
      matches = ExtractMarkdownLinksAndImages.extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
      self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
       matches = ExtractMarkdownLinksAndImages.extract_markdown_links(
          "This is a text with a [link](https://www.mambastyle.com)"
    )
       self.assertListEqual([("link", "https://www.mambastyle.com")],matches)
    
    


if __name__ == "__main__":
    unittest.main()