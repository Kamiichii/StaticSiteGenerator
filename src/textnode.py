from enum import Enum
from HTMLNode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC ="italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"

class TextNode:
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self,other):
        if(self.text == other.text and 
           self.text_type == other.text_type and 
           self.url == other.url):
        
            return True
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
    
def text_node_to_html_node(text_node):
         if text_node.text_type == TextType.NORMAL:
              return LeafNode(None,text_node.text)
         elif text_node.text_type == TextType.BOLD:
              return LeafNode("b",text_node.text)
         elif text_node.text_type == TextType.ITALIC:
              return LeafNode("i",text_node.text)
         elif text_node.text_type == TextType.CODE:
              return LeafNode("code",text_node.text)
         elif text_node.text_type == TextType.LINKS:
              return LeafNode("a",text_node.text,{"href":f"{text_node.url}"})
         elif text_node.text_type == TextType.IMAGES:
              return LeafNode("img","", {"src":f"{text_node.url}","alt":f"{text_node.text}"})
         raise ValueError(f"Invalid text type: {text_node.text_type}")
    
    
