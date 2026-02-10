import unittest
from split_blocks import markdown_to_blocks, block_to_block_type, extract_title, BlockType 

class TestMarkdownToBlocks(unittest.TestCase):
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
            ]
        )

    def test_empty_lines(self):
        md = """
This is the first line





     This is the second line.    

     
- This is a list 
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first line",
                "This is the second line.",
                "- This is a list",
            ]
        )

class TestBlockTypes(unittest.TestCase):
    def test_heading_block(self):
        block = "### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_incorrect_heading(self):
        block = "###This is not a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_code_block(self):
        block ="```This is a code block \nHere is more code\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_incorrect_code_block(self):
        block = "``This is a code block ```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_quote_block(self):
        block = "> This is\n> A\n>Quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- This is a list\n- Here is another part"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. Here\n2. Is \n3. A \n4. List"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

class TestExtractTitle(unittest.TestCase):
    def test_multiple_headers(self):
        md = """
# This is a title
## This is not a title
### This is just a header

- This is a list
- Of stuff
"""
        self.assertEqual(extract_title(md), "This is a title")

    def test_no_title(self):
        md = """
## This is not a title
### This also isn't a title
"""
        with self.assertRaises(Exception) as cm:
            title = extract_title(md)
        self.assertEqual(str(cm.exception), "No title found")

if __name__ == "__main__":
    unittest.main()