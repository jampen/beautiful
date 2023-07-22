from src.list import BulletPointBuilder
from src.style import Style

# Create the style for the bullet point
bullet_style = Style(
    color_name='blue'
)

# Builders allow us to easily replicate configurations of our elements
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
