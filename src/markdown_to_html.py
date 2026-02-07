from split_blocks import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def text_to_children(text):
    children = []

    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        child = text_node_to_html_node(node)
        children.append(child)

    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        # Determine the type of block
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            text = block.lstrip(("#"))
            hash_count = len(block) - len(text)
            text = text.lstrip()
            children = text_to_children(text)

            heading_node = ParentNode(f"h{hash_count}", children)
            html_nodes.append(heading_node)

        
        elif block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            children = text_to_children(text)
            paragraph_node = ParentNode(f"p", children)
            html_nodes.append(paragraph_node)

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_text = ""
            for line in lines:
                if line.startswith("> "):
                    new_text += line[2:]
                elif line.startswith(">"):
                    new_text += line[1:]
                new_text += "\n"

            new_text = new_text.rstrip("\n")
            children = text_to_children(new_text)
            quote_node = ParentNode(f"blockquote", children)
            html_nodes.append(quote_node)

        elif block_type == BlockType.CODE:
            text = block.replace("```", "")
            text = text.lstrip("\n")
            text_node = TextNode(text, TextType.CODE)
            code_node = text_node_to_html_node(text_node)
            pre_node = ParentNode("pre", [code_node])
            html_nodes.append(pre_node)

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                if not line.strip():
                    continue
                index = line.index(".")
                text = line[index+2:]
                child = text_to_children(text)
                list_item = ParentNode("li", child)
                list_items.append(list_item)

            ordered_list = ParentNode("ol", list_items)
            html_nodes.append(ordered_list)

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                text = line[2:]
                child = text_to_children(text)
                list_item = ParentNode("li", child)
                list_items.append(list_item)

            unordered_list = ParentNode("ul", list_items)
            html_nodes.append(unordered_list)

    div_node = ParentNode("div", html_nodes)
    return div_node



    
