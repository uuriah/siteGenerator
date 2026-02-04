import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType
    
class TestTextToHTMLNode(unittest.TestCase):
    def test_eq_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_eq_bold(self):
        node = TextNode("This is text with **bold** font", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" font", TextType.TEXT)
        ])

    def test_invalid_syntax(self):
        with self.assertRaises(Exception) as cm:
            node = TextNode("This is invalid **markdown* syntax", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(cm.exception), "invalid markdown, formatted section not closed")


    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

        

if __name__ == "__main__":
    unittest.main()

