from src.element import Element
from src.style import Style
from src.icon import Icon

from copy import deepcopy


class ListedElements:
    def __init__(self, elements, title):
        self.elements = elements
        self.title = title

    def rendered(self):
        renderings = [element.rendered() for element in self.elements]
        if self.title != None:
            renderings.insert(0, self.title.rendered())
        return '\n'.join(renderings)


class BulletPointBuilder:
    def __init__(self, style=None):
        self.style = style

        if self.style is None:
            self.style = Style()

    def create_bullet_points(self, list, title=None):
        elements = []
        element_style = deepcopy(self.style)
        element_style.start_icon = Icon('● ', self.style.start_icon.color_name)
        element_style.end_icon = Icon()

        for item in list:
            elements.append(Element(item, element_style))

        return ListedElements(elements, title=title)
