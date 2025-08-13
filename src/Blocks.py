from enum import Enum
from htmlnode import HTMLNode,ParentNode
from split_nodes_delimiter import text_to_textnodes
from textnode import TextNode,TextType
import textwrap
import re

class BlockTypes(Enum):
    PARAGRAPH_BLOCK = "paragraph"
    HEADING_BLOCK = "heading"
    CODE_BLOCK = "code_b"
    QUOTE_BLOCK = "quote"
    UNORDERED_LIST = "uolist"
    ORDERED_LIST = "olist"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks_finished = []
    for block in blocks:
        stripped_block =block.strip()
        if stripped_block:
            blocks_finished.append(stripped_block)
    return blocks_finished

def block_to_block_type(markdown):
    if re.match(r"^#{1,6}",markdown):
        return BlockTypes.HEADING_BLOCK
    elif re.match(r"^```.*```$",markdown,re.DOTALL):
        return BlockTypes.CODE_BLOCK
    elif re.match(r"^>.*?(?:\n>.*?)*$",markdown):
        return BlockTypes.QUOTE_BLOCK
    elif re.match(r"^- .*?(?:\n- .*?)*$",markdown):
        return BlockTypes.UNORDERED_LIST
    elif re.match(r'^\d+\. ', markdown):
        lines = markdown.split("\n")
        for i, line in enumerate(lines, 1):
            if not re.match(rf'^{i}\. ', line):
                return BlockTypes.PARAGRAPH_BLOCK
        return BlockTypes.ORDERED_LIST
    else:
        return BlockTypes.PARAGRAPH_BLOCK
    
def text_to_child_node(text):
    text_nodes = text_to_textnodes(text)
    child_nodes = []
    for text_node in text_nodes:
        child_nodes.append(TextNode.text_node_to_html_node(text_node))
    return child_nodes

def qblock_to_html_node(text):
    items = text.split("\n")
    child_nodes = []
    for item in items:
        if item[1:].strip():
           child_nodes.extend(text_to_child_node(item[1:].strip()))
    return ParentNode(tag="blockquote",children=child_nodes)

def ulist_to_html_node(text):
    items = text.split("\n")
    child_nodes = []
    for item in items:
        child_nodes.append(ParentNode(tag="li",children=text_to_child_node(item[2:])))
    return ParentNode(tag="ul",children=child_nodes)


def olist_to_html_node(text):
    items = text.split("\n")
    child_nodes = []
    for item in items:
        child_nodes.append(ParentNode(tag="li",children=text_to_child_node(item[3:])))
    return ParentNode(tag="ol",children=child_nodes)

        

def heading_to_html_node(markdown):
    counter = 0
    for character in markdown:
        if character == '#':
            counter += 1
        else:
            break
    if counter > 6:
        raise ValueError("Heading cant have more than 6 hashes")
    return ParentNode(tag=f"h{counter}",children=text_to_child_node(markdown[counter:].strip()))

def paragraph_to_html_node(text):
    lines = text.split("\n")
    paragraph_text = " ".join(lines)
    paragraph_text = re.sub(r"\s+", " ", paragraph_text) 
    child_nodes = text_to_child_node(paragraph_text)
    return ParentNode(tag="p",children=child_nodes)

def code_to_html_node(text):
    text_new = text[3:-3]
    text_new = text_new.lstrip("\n") 
    text_new = textwrap.dedent(text_new)
    html_node = TextNode.text_node_to_html_node(TextNode(text_new,TextType.PLAIN_TEXT))
    outter =  ParentNode("code",[html_node])
    return ParentNode("pre",[outter])

def block_to_html_node(markdown,block_type):
    if block_type == BlockTypes.QUOTE_BLOCK:
        return qblock_to_html_node(markdown)
    if block_type == BlockTypes.UNORDERED_LIST:
        return ulist_to_html_node(markdown)
    if block_type == BlockTypes.ORDERED_LIST:
        return olist_to_html_node(markdown)
    if block_type == BlockTypes.HEADING_BLOCK:
        return heading_to_html_node(markdown)
    if block_type == BlockTypes.PARAGRAPH_BLOCK:
        return paragraph_to_html_node(markdown)
    if block_type == BlockTypes.CODE_BLOCK:
        return code_to_html_node(markdown)
    else:
        raise TypeError("Given block type is not recognized")
    

    


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    chlidren = []
    for block in blocks:
        type_of_block = block_to_block_type(block)
        chlidren.append(block_to_html_node(block,type_of_block))
    return ParentNode("div",chlidren)

        
