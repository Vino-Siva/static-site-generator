import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_has_title(self):
        test_md_1 = """
# this is an h1

this is paragraph text

## this is an h2
"""
        self.assertEqual(extract_title(test_md_1), "this is an h1")

    def test_no_title(self):
        test_md_2 = """
            This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        self.assertRaises(Exception, extract_title, test_md_2)

    def test_whitespace_title(self):
        test_md_3 = """
 #     this is an h1

this is paragraph text

## this is an h2
"""
        self.assertEqual(extract_title(test_md_3), "this is an h1")

    def test_empty_title(self):
        test_md_4 = " "
        self.assertRaises(Exception, extract_title, test_md_4)


if __name__ == "__main__":
    unittest.main()
