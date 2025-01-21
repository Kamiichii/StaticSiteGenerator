import re

def extract_markdown_images(text):
    tuples_list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)       
    return tuples_list

def extract_markdown_links(text):
    tuples_list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuples_list



