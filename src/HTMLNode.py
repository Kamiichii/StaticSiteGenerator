class HTMLNode:
    def __init__(self,tag = None,value = None,childeren = None,props = None):
        self.tag = tag
        self.value =value
        self.childeren = childeren
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
          return " ".join(f'"{key}": "{value}"' for key, value in self.props.items())
    
    def __eq__(self,other):
         if(self.tag == other.tag and
            self.value == other.value and
            self.childeren == other.childeren and
            self.props == other.props):
              return True
         
    def __repr__(self):
         return f"HTMLNode({self.tag},{self.value},{self.childeren},{self.props})"

