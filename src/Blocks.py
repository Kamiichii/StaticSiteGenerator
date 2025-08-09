def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks_finished = []
    for block in blocks:
        stripped_block =block.strip()
        if stripped_block:
            blocks_finished.append(stripped_block)
    return blocks_finished


