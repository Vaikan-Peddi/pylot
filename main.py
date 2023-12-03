# required to build a class for DOM_object and a tree for representing and manipulating 
# the PyDOM.

class DOMObject:
    def __init__(self, tag, attributes=None, content=None, self_closing=False):
        self.tag = tag
        self.attributes = attributes or {}
        self.content = content or []
        self.self_closing = self_closing
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        attribute_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        if attribute_str:
            attribute_str = ' ' + attribute_str

        content_str = ''

        if not self.self_closing:
            content_str = ''.join([str(item) for item in self.content])

        if self.self_closing:
            return f'<{self.tag}{attribute_str} />'
        else:
            children_str = ''.join([str(child) for child in self.children])
            return f'<{self.tag}{attribute_str}>{content_str}{children_str}</{self.tag}>'


# Example usage:
html = DOMObject('html')
head = DOMObject('head')
title = DOMObject('title', content=['Pylot'])
body = DOMObject('body', attributes={'bgcolor': 'aqua'})

h1 = DOMObject('h1', content=['My first Pylot page'])
p = DOMObject('p', content=['This is a simple HTML page.'])

br = DOMObject('br', self_closing=True)
img = DOMObject('img', attributes={'src': 'example.jpg', 'alt': 'Example Image'}, self_closing=True)

ul = DOMObject('ul')
li1 = DOMObject('li', content=['Item 1'])
li2 = DOMObject('li', content=['Item 2'])
li3 = DOMObject('li', content=['Item 3'])

ul.children.extend([li1, li2, li3])

head.children.append(title)

body_content = [h1, p, br, img, ul]
body.children.extend(body_content + body_content)

html.children.extend([head, body])


print(html)


with open("pages/index.html", 'w+') as index:
    index.write(str(html))