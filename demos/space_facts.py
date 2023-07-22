# To create a title
from src.title import TitleBuilder

# To add an icon to our title
from src.icon import Icon

from src.list import BulletPointBuilder
from src.style import Style

# Create the style for the bullet point
bullet_style = Style(
    color_name='blue'
)

# Create the style for the title
title_style = Style(
    color_name='yellow',
    start_icon=Icon(graphic='🚀 '),
    end_icon=Icon(graphic=' 🌌')
)

# Builders allow us to easily replicate configurations of our elements
bullet_point_builder = BulletPointBuilder(style=bullet_style)
title_builder = TitleBuilder(style=title_style)

# Create our space-related bullet points
space_facts = bullet_point_builder.create_bullet_points(
    list=[
        'The Milky Way galaxy contains over 100 billion stars.',
        'A day on Venus is longer than a year on Venus.',
        'The Sun makes up about 99.86% of the mass in our solar system.',
        'The first human-made object to reach space was the Soviet satellite Sputnik 1 in 1957.',
        'Neutron stars are so dense that a sugar-cube-sized amount of neutron star material would weigh about as much as Mount Everest.'
    ],
    title=title_builder.create_title('Fascinating Space Facts')
)

# Assign each style like this
space_facts.elements[0].style.color_name = 'orange'
space_facts.elements[0].style.start_icon.color_name = 'orange'

space_facts.elements[1].style.color_name = 'green'
space_facts.elements[1].style.start_icon.color_name = 'green'

space_facts.elements[2].style.color_name = 'yellow'
space_facts.elements[2].style.start_icon.color_name = 'yellow'

space_facts.elements[3].style.color_name = 'cyan'
space_facts.elements[3].style.start_icon.color_name = 'cyan'

space_facts.elements[4].style.color_name = 'magenta'
space_facts.elements[4].style.start_icon.color_name = 'magenta'

# Draw our text to the screen
print(space_facts.rendered())
