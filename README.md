# Beautiful 🐍
An easy to use python library for colorful UI
# Example usage
## 1. Creating a congratulations message (demos/title.py)
This example will show you how to set up a basic style for creating colored titles. We 
```py
from src.title import TitleBuilder
from src.style import Style
from src.icon import Icon

# Create our style
title_style = Style(
    color_name='orange',
    start_icon=Icon(graphic='⭐ ')
)

# So that we may re-use our configuration
title_builder = TitleBuilder(style=title_style)

# Create our messages
congratulations = title_builder.create_title('Congratulations!')
well_done = title_builder.create_title('Well done!')

# Draw our text to the screen
print(congratulations.rendered())
print(well_done.rendered())
```
### Result of this example:
![Example usage, showing two lines of orange text, 'Congratulations!' and 'Well done!', with a star graphic at the beginning](/demos/title_py_result.png "Our result")
## 2. Creating a bullet list (demos/bullet.py)
```py
from src.list import BulletPointBuilder
from src.style clearimport Style

# Create the style for the bullet point
bullet_style = Style(
    color_name='blue'
)

#Builders allow us to easily replicate configurations of our elements
bullet_point_builder = BulletPointBuilder(style=bullet_style)

# We can easily create bullet points
fruits = bullet_point_builder.create_bullet_points(
    list=[
        '🍎 Apple',
        '🍊 Orange',
        '🍐 Pear',
        '🥝 Kiwi',
        '🥭 Mango'
    ])

# Draw our text to the screen
print(fruits.rendered())
```
### Result of this example:
![Example usage, showing a bullet point list of an assortment of fruits](/demos/bullet_py_result.png "Our result")

## 2.1 Adding a title to our bullet point list (demos/bullet_titled.py)
```py
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
```
### Result of this example:
![Example usage, showing a bullet point list of rainbows, with the title having a start icon of a raining cloud and an end icon of a sun"](/demos/bullet_titled_py_result.png "Our result")
## 2.2 Adding colors to each bullet point (demos/bullet__colored)
```py
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
```
### Result of this example:
![Example usage, showing a bullet point list of rainbows, with the title having a start icon of a raining cloud and an end icon of a sun, and each item in the bullet point colored properly"](/demos/bullet_colored_py_result.png "Our result")