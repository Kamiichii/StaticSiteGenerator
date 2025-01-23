from textnode import *
from extract_markdown_images_or_texts import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_node_list = []

    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            parts = node.text.split(delimiter)

            if len(parts) % 2 == 0:
                raise ValueError("Missing closing delimiter")
            
            for i, text in enumerate(parts):
                if text != "":  
                    if i % 2 == 0:
                        new_node_list.append(TextNode(text, TextType.NORMAL))
                    else:
                        new_node_list.append(TextNode(text, text_type))

        else:
            new_node_list.append(node)
    return new_node_list

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)

        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        if images == []:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text

        for image in images:
            image_alt = image[0]
            image_link = image[1]


            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.NORMAL))            
            new_nodes.append(TextNode(image_alt,TextType.IMAGES,image_link))
            remaining_text = sections[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,TextType.NORMAL))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text

        for link in links:
            link_alt = link[0]
            this_link = link[1]


            sections = remaining_text.split(f"[{link_alt}]({this_link})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.NORMAL))
            
            new_nodes.append(TextNode(link_alt,TextType.LINKS,this_link))
            remaining_text = sections[1]
            
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,TextType.NORMAL))
    return new_nodes
            


        

    
    










            

