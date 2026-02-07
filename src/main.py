from textnode import TextNode
from textnode import TextType
from copy_contents import remove_public_content, copy_content

def main():
    textNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    print(textNode)

    remove_public_content("./public")
    copy_content("./static", [])

if __name__ == "__main__":
    main()