from textnode import TextType,TextNode
from copier import copy_content_to_public
from page_generation import generate_pages_recursive


def main():
   copy_content_to_public("./static")
   generate_pages_recursive("content","template.html","public")

main()