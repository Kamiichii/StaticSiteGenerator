from textnode import TextType,TextNode
from copier import copy_content_to_public
from page_generation import generate_pages_recursive
from sys import argv


def main():
   if (argv[1]):
      basepath = argv[1]
   else:
      basepath = "/"


   copy_content_to_public("./static")
   generate_pages_recursive(basepath,"content","template.html","docs")

main()