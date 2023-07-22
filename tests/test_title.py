from src.title import TitleBuilder
from src.element import Element


def test_title_builder_create_title_returns_element():
    title_builder = TitleBuilder()
    title = title_builder.create_title('hello')
    assert isinstance(title, Element)
