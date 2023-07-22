from src.style import Style
from src.icon import Icon
from src.title import TitleBuilder

if __name__ == '__main__':
    title_style = Style(
        color_name='red',
        # Optional!
        start_icon=Icon('◄ ', color_name='cyan'),
        end_icon=Icon(' ►', color_name='magenta'),
    )

    title_builder = TitleBuilder(
        style=title_style
    )

    main_title = title_builder.create_title('My program')
    options_title = title_builder.create_title('Options')
    credits_title = title_builder.create_title('Credits')

    print(main_title.rendered())
    print(options_title.rendered())
    print(credits_title.rendered())
    pass
