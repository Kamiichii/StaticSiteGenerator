from textnode import TextType,TextNode


def main():
    text_node = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    print(text_node)

main()