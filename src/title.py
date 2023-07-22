from src.element import Element
from src.style import Style


class TitleBuilder:
    def __init__(self, style=None):
        self.style = style

        if self.style is None:
            self.style = Style()

    def create_title(self, text):
        title = Element(text, self.style)
        return title
