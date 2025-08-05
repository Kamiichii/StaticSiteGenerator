class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
       if not isinstance(other, HTMLNode):
           return False
       return (
           self.tag == other.tag
           and self.value == other.value
           and self.children == other.children
           and self.props == other.props
       )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None ,props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("The leaf has  to have a value")

        if not self.tag:
            return f"{self.value}"
        
        if self.props is not None:
            props_html = self.props_to_html() 
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("The parentnode has to have a tag")
        
        if self.children is None:
            raise ValueError("The parentnode has to have a children")
        
        children_combined = str()
        for child in self.children:

            children_combined = children_combined + (child.to_html())

        return f"<{self.tag}>" + children_combined + f"</{self.tag}>"
        
