from textnode import TextType,TextNode
from extract_markdown_links_and_images import ExtractMarkdownLinksAndImages

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_node_list = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            text_node_list.append(node)
            continue
        non_empty_nodes = []
        new_nodes = node.text.split(delimiter)
        if len(new_nodes) % 2 == 0:            
            raise Exception("Unmatched delimiter found in text: " + node.text)
        for i in range(len(new_nodes)):
            if new_nodes[i] == "":
                continue
            if i % 2 != 0:
                non_empty_nodes.append(TextNode(new_nodes[i],text_type))
            else:
                non_empty_nodes.append(TextNode(new_nodes[i],TextType.PLAIN_TEXT))            
        text_node_list.extend(non_empty_nodes)
       
    return text_node_list

def split_nodes_image(old_nodes):
    image_node_list = []
    for node in old_nodes:
        if node.text_type == TextType.IMAGE_TEXT:
            image_node_list.append(node)
            continue
        images_and_text = ExtractMarkdownLinksAndImages.extract_markdown_images(node.text)
        if not images_and_text:
            image_node_list.append(node)
            continue
        current_text = node.text
        for pair in images_and_text:
            current_text = current_text.split(f"![{pair[0]}]({pair[1]})",1)
            if current_text[0]:
                image_node_list.append(TextNode(current_text[0],TextType.PLAIN_TEXT))
            image_node_list.append(TextNode(pair[0],TextType.IMAGE_TEXT,pair[1]))
            current_text = current_text[1]
        if current_text:
            image_node_list.append(TextNode(current_text,TextType.PLAIN_TEXT))
    return image_node_list

def split_nodes_link(old_nodes):
    link_node_list = []
    for node in old_nodes:
        if node.text_type == TextType.LINK_TEXT:
            link_node_list.append(node)
            continue
        links_and_text = ExtractMarkdownLinksAndImages.extract_markdown_links(node.text)
        if not links_and_text:
            link_node_list.append(node)
            continue
        current_text = node.text
        for pair in links_and_text:
            current_text = current_text.split(f"[{pair[0]}]({pair[1]})",1)
            if current_text[0]:
                link_node_list.append(TextNode(current_text[0],TextType.PLAIN_TEXT))
            link_node_list.append(TextNode(pair[0],TextType.LINK_TEXT,pair[1]))
            current_text = current_text[1]
        if current_text:
            link_node_list.append(TextNode(current_text,TextType.PLAIN_TEXT))
    return link_node_list

            



