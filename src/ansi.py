
class InvalidColorError (Exception):
    def __init__(self, message):
        super().__init__(message)


class ANSI:
    COLOR_ANSI = {
        'white': '\u001b[37m',
        'grey': '\u001b[38;5;243m',
        'darkgrey': '\u001b[38;5;233m',
        'black':  '\u001b[30m',
        'red':    '\u001b[31m',
        'green':  '\u001b[32m',
        'yellow': '\u001b[33m',
        'blue':   '\u001b[34m',
        'magenta': '\u001b[35m',
        'cyan':   '\u001b[36m',
        'orange': '\u001b[38;5;208m',
        'darkorange': '\u001b[38;5;130m',
        'darkgreen': '\u001b[38;5;28m',
    }

    RESET_ANSI = '\u001b[0m'

    def get_color_ansi(color_name):
        if color_name in ANSI.COLOR_ANSI:
            return ANSI.COLOR_ANSI[color_name]
        else:
            raise InvalidColorError(f'color name: "{color_name}" is invalid')

    def reset_after_use(text):
        return f'{ANSI.RESET_ANSI}{text}{ANSI.RESET_ANSI}'
