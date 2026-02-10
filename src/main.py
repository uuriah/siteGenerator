from textnode import TextNode
from textnode import TextType
from copy_contents import remove_public_content, copy_content
from generate_page import generate_pages_recursively
import sys

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    remove_public_content("./docs")
    copy_content("./static", [])

    print(generate_pages_recursively("content", "template.html", "docs", [], basepath))

if __name__ == "__main__":
    main()