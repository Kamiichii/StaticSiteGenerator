import unittest

from page_generation import extract_title


class TestPageGeneration(unittest.TestCase):
    def test_extract_title_one_hash(self):
        markdown = "# Umbambe"
        result = extract_title(markdown)
        self.assertEqual(result,"Umbambe")
    def test_extract_title_multiple_hash(self):
        markdown = "### hamsikoli\n#Umbambe"
        result = extract_title(markdown)
        self.assertEqual(result,"Umbambe")
    def test_extract_title_multiple_titles(self):
        markdown = "# Umbambe\n#Hamsikoli"
        result = extract_title(markdown)
        self.assertEqual(result,"Umbambe")


if __name__ == "__main__":
    unittest.main()