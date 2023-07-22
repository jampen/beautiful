from src.ansi import ANSI


class Icon:
    def __init__(self, graphic='', color_name='white'):
        self.graphic = graphic
        self.color_name = color_name

    def rendered(self):
        color = ANSI.get_color_ansi(self.color_name)
        return ANSI.reset_after_use(f'{color}{self.graphic}')
