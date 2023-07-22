from src.ansi import (ANSI, InvalidColorError)
import pytest


def test_ansi_reset_is_correct():
    correct_reset = '\u001b[0m'
    assert ANSI.RESET_ANSI == correct_reset


def test_get_color_ansi_returns_ansi_code():
    assert ANSI.get_color_ansi('white') == ANSI.COLOR_ANSI['white']


def test_get_color_ansi_raises_InvalidColorError_on_invalid_input():
    with pytest.raises(InvalidColorError):
        assert ANSI.get_color_ansi('invalid color')


def test_reset_after_use_will_reset_styles():
    string = ANSI.reset_after_use('hello')
    assert string.startswith(ANSI.RESET_ANSI)
    assert string.endswith(ANSI.RESET_ANSI)
