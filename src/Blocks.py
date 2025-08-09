from enum import Enum
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
    elif re.match(r"^```.*```$",markdown):
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
