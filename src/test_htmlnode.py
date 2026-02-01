import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a", "This is a link", None, {"href": "https://google.com", "target": "_blank",})
        node2 = HTMLNode("a", "This is a link", None, {"href": "https://google.com", "target": "_blank",})

        self.assertEqual(node1, node2)

    def test_eq_2(self):
        node1 = HTMLNode("p", "This is a paragraph", None, None)
        node2 = HTMLNode("p", "This is a paragraph", None, None)

        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HTMLNode("p", "This is a paragraph", None, None)
        node2 = HTMLNode("a", "This is a link", None, {"href": "https://google.com", "target": "_blank",})

        self.assertNotEqual(node1, node2)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_title(self):
        node = LeafNode("title", "This is a Title!")
        self.assertEqual(node.to_html(), "<title>This is a Title!</title>")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_parent(self):
        grandchild_node = LeafNode("b", "grandchild") 
        self.assertEqual(grandchild_node.to_html(), "<b>grandchild</b>")
    
    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("p", "great grandchild")
        grandchild_node = ParentNode("b", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b><p>great grandchild</p></b></span></div>")

if __name__ == "__main__":
    unittest.main()