import re 
from enum import Enum

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
    
        