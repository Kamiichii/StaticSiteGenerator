from textnode import *

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







            

