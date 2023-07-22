from src.icon import Icon
from src.ansi import ANSI


def test_icon_rendering_is_reset():
    icon = Icon('x', color_name='red')
    rendering = icon.rendered()
    assert rendering.startswith(ANSI.RESET_ANSI)
    assert rendering.endswith(ANSI.RESET_ANSI)
