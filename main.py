# required to build a class for DOM_object and a tree for representing and manipulating 
# the PyDOM.

class DOMObject:
    def __init__(self, tag, attributes=None, content=None, self_closing=False):
        self.tag = tag
        self.attributes = attributes or {}
        self.content = content or []
        self.self_closing = self_closing

    def add_child(self, child):
        self.content.append(child)

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
            return f'<{self.tag}{attribute_str}>{content_str}</{self.tag}>'


def domify():
    html = DOMObject('html')
    head = DOMObject('head')
    title = DOMObject('title', content=['My HTML Page'])
    body = DOMObject('body', attributes={'bgcolor': 'aqua'})

    h1 = DOMObject('h1', content=['Hello, World!'])
    p = DOMObject('p', content=['This is a simple HTML page.'])

    br = DOMObject('br', self_closing=True)
    img = DOMObject('img', attributes={'src': 'example.jpg', 'alt': 'Example Image'}, self_closing=True)

    ul = DOMObject('ul')
    li1 = DOMObject('li', content=['Item 1'])
    li2 = DOMObject('li', content=['Item 2'])
    li3 = DOMObject('li', content=['Item 3'])

    ul.add_child(li1)
    ul.add_child(li2)
    ul.add_child(li3)

    head.add_child(title)
    body.add_child(h1)
    body.add_child(p)
    body.add_child(br)
    body.add_child(img)
    body.add_child(ul)

    html.add_child(head)
    html.add_child(body)

    return html

html_tree = domify()
print(html_tree)
