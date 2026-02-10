from markdown_to_html import markdown_to_html_node
from htmlnode import ParentNode, LeafNode, HTMLNode
from split_blocks import extract_title
import os 

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)

    html_string = ParentNode.to_html(html_node)

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_path_without_index = dest_path.replace("index.md", "")
    if not os.path.exists(dest_path_without_index):
        os.makedirs(dest_path_without_index, exist_ok=True)

    fullpath = dest_path.replace("index.md", "index.html")
    with open(fullpath, "w") as f:
        f.write(template)

    return "Page successfully generated"

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, visited, basepath):

    # create list of all files/dirs in content directory
    content_list = os.listdir(dir_path_content)

    for item in content_list:
        fullpath = os.path.join(dir_path_content, item)
        if os.path.isdir(fullpath):

            if fullpath not in visited:
                generate_pages_recursively(fullpath, template_path, dest_dir_path, visited, basepath)

        elif os.path.isfile(fullpath):
            dest_path = fullpath.replace("content", "docs")
            generate_page(fullpath, template_path, dest_path, basepath)

            visited.append(fullpath)

    return

            





