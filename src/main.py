from textnode import TextType,TextNode
from copier import copy_content_to_public
from page_generation import generate_page


def main():
   copy_content_to_public("./static")
   generate_page("content/index.md","template.html","public/index.html")

main()