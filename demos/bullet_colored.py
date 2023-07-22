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


# Assign each style like this
# We can set the color of the bullet point using the start_icon.color_name property of the style.
colors.elements[0].style.color_name = 'red'
colors.elements[0].style.start_icon.color_name = 'red'

colors.elements[1].style.color_name = 'orange'
colors.elements[1].style.start_icon.color_name = 'orange'

colors.elements[2].style.color_name = 'green'
colors.elements[2].style.start_icon.color_name = 'green'

colors.elements[3].style.color_name = 'blue'
colors.elements[3].style.start_icon.color_name = 'blue'

colors.elements[4].style.color_name = 'purple'
colors.elements[4].style.start_icon.color_name = 'purple'


# Draw our text to the screen
print(colors.rendered())
