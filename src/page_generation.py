import re 
import os
import pathlib
from Blocks import markdown_to_html_node 


def extract_title(markdown):
    
    h1 = re.findall(r"^#(?!#) *(.*?)$",markdown,re.MULTILINE)
    if not h1:
        raise Exception("Couldnt find a title")
    else:
        return h1[0].strip()

def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as from_file:
        from_file_contents = from_file.read()
    with open(template_path, "r") as template_file:
        template_contents = template_file.read()
    html = markdown_to_html_node(from_file_contents).to_html()
    title = extract_title(from_file_contents)
    new_template = template_contents.replace("{{ Title }}",title).replace("{{ Content }}",html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as dest_file:
      dest_file.write(new_template)

def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):
    
    for name in os.listdir(dir_path_content):
        dir_path = os.path.join(dir_path_content,name)
        dest_path = os.path.join(dest_dir_path,name)
        if os.path.isdir(dir_path):
            generate_pages_recursive(dir_path,template_path,dest_path)
        elif re.match(r"(.*?).md$",name):
            dest_path = pathlib.Path(dest_path).with_suffix(".html")
            generate_page(dir_path, template_path, dest_path)
            