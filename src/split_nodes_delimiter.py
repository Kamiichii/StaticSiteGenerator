from textnode import TextType,TextNode


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
