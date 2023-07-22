# To create a title
from src.title import TitleBuilder

# To add an icon to our title
from src.icon import Icon

from src.list import BulletPointBuilder
from src.style import Style

# Create the style for the bullet point
bullet_style = Style(
    color_name='grey'
)

# Create the style for the title
title_style = Style(
    color_name='green',
    start_icon=Icon(graphic='🌧  '),
    end_icon=Icon(graphic=' 🌞')
)

# Builders allow us to easily replicate configurations of our elements
bullet_point_builder = BulletPointBuilder(style=bullet_style)
title_builder = TitleBuilder(style=title_style)

# Create our colors
colors = bullet_point_builder.create_bullet_points(
    list=[
        'Red',
        'Orange',
        'Green',
        'Blue',
        'Purple'
    ],
    # 'title' is optional here, it can be any Element
    title=title_builder.create_title('Rainbow')
)

# Draw our text to the screen
print(colors.rendered())
