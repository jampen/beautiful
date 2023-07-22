from copy import deepcopy
from src.style import Style


class Element:
    def __init__(self, text='', style=Style()):
        self.text = text
        self.style = deepcopy(style)

    def rendered(self):
        icon_texts = self.style.get_icon_texts()
        string = str()
        string += icon_texts[0]
        string += self.style.get_color_ansi()
        string += str(self.text)
        string += icon_texts[1]
        return string
