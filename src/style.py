from src.ansi import ANSI
from src.icon import Icon


class Style:
    def __init__(self, **kwargs):
        self.color_name = 'white'
        self.start_icon = Icon()
        self.end_icon = Icon()

        if 'color_name' in kwargs:
            self.color_name = kwargs['color_name']

        if 'start_icon' in kwargs:
            self.start_icon = kwargs['start_icon']

        if 'end_icon' in kwargs:
            self.end_icon = kwargs['end_icon']

    def get_color_ansi(self):
        return ANSI.get_color_ansi(self.color_name)

    def get_icon_texts(self):
        return [self.start_icon.rendered(), self.end_icon.rendered()]
