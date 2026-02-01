
class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            output = ""
            for key, val in self.props.items():
                output += f' {key}="{val}"'
            return output
        
        return None
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props_to_html() == other.props_to_html():
            return True

        else:
            return False
        
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("Node value is missing.")
        
        if self.tag == None:
            return f"{self.value}"
        
        else:
            if self.props == None:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props_to_html()})" 
    
class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag == None:
            raise ValueError("Node tag is missing.")
        
        if self.children == None:
            raise ValueError("Node children is missing.")
        
        l_tag = f"<{self.tag}>"
        r_tag = f"</{self.tag}>"
        middle = ""
        
        for child in self.children:
            if type(child) == ParentNode:
                middle = child.to_html()
            else:
                middle += f'<{child.tag}>{child.value}</{child.tag}>'
        
        return l_tag + middle + r_tag
    



        
