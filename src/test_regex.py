import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links

class TestRegex(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_no_matching_images_found(self):
        matches = extract_markdown_images(
            "This is text without an !image(catpic.jpeg)"
        )
        self.assertListEqual([], matches)

    def test_no_matching_links_found(self):
        matches = extract_markdown_links(
            "This is text without any link to youtube](https://www.youtube.com)"
        )
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()