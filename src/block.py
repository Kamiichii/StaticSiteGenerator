import re 
from enum import Enum
from extract_markdown_images_or_texts import markdown_to_blocks
from ParentNode import ParentNode
from Splitnodes import text_to_textnodes
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

    

def block_to_block_type(block):
    if re.match(r"^#{1,6}",block):
        return BlockType.HEADING
    elif re.match(r'^```[\s\S]*```$',block):
        return BlockType.CODE
    elif re.match(r"^>.*$(\n^>.*$)*$",block ,re.MULTILINE):
        return BlockType.QUOTE
    elif re.match(r"^(\*|-) .*$(\n^(\*|-) .*$)*$",block, re.MULTILINE):
        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        lines = block.split("\n")
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
    
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    
    if block_type == BlockType.PARAGRAPH:
        lines = block.split("\n")
        paragraph = " ".join(lines)
        children = text_to_children(paragraph)
        return ParentNode("p",children)
    
    elif block_type == BlockType.HEADING:
        level = 0
        for char in block:
            if char == "#":
                level += 1
            else:
                break
        if level + 1 >= len(block):
            raise ValueError
        text = block[level+1 :]
        children = text_to_children(text)
        return ParentNode(f"h{level}",children)
    
    elif block_type == BlockType.CODE:
        text = block[4:-3]
        children = text_to_children(text)
        code = ParentNode("code",children)
        return ParentNode("pre",[code])
    
    elif block_type == BlockType.ORDERED_LIST:
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item[3:]
            children = text_to_children(text)
            html_items.append(ParentNode("li",children))
        return ParentNode("ol",html_items)
    
    elif block_type == BlockType.UNORDERED_LIST:
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item[2:]
            children = text_to_children(text)
            html_items.append(ParentNode("li",children))
        return ParentNode("ul",html_items)
    
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            if not line.startswith(">"):
                raise ValueError("Invalid quote block")
            new_lines.append(line.lstrip(">").strip())
        content = " ".join(new_lines)
        children = text_to_children(content)
        return ParentNode("blockquote",children)
    
    else:
        raise ValueError("Invalid block type")

    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div",children,None)
        
        