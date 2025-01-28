import re


def extract_markdown_images(text):
    tuples_list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)       
    return tuples_list

def extract_markdown_links(text):
    tuples_list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuples_list

def markdown_to_blocks(markdown):

    raw_blocks = markdown.split('\n\n')
    blocks = []

    for block in raw_blocks:
        if block != "":
            blocks.append(block.strip())
    
    return blocks


    
     
