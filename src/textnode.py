from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT ="italic"
    CODE_TEXT = "code"
    LINKS = "link"
    IMAGES = "image"

class TextNode:
    def __init__(self,text,text_type,url):
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