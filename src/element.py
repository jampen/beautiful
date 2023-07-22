class Element:
    def __init__(self, text, style):
        self.text = text
        self.style = style

    def rendered(self):
        icon_texts = self.style.get_icon_texts()
        string = str()
        string += icon_texts[0]
        string += self.style.get_color_ansi()
        string += self.text
        string += icon_texts[1]
        return string
