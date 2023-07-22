from src.style import Style
from src.icon import Icon
from src.title import TitleBuilder
from src.list import BulletPointBuilder

if __name__ == '__main__':
    """Styles define the colour and attributes of our UI elements"""
    title_style = Style(
        color_name='grey',

        # Icons give our titles a flair
        start_icon=Icon('◄ ', color_name='blue'),
        end_icon=Icon(' ►', color_name='blue'),
    )

    bullet_style = Style(
        color_name='white'
    )

    """Builders allow us to easily replicate configurations of our elements"""
    title_builder = TitleBuilder(style=title_style)
    bullet_point_builder = BulletPointBuilder(style=bullet_style)

    """ We can easily create bullet points"""
    fruits = bullet_point_builder.create_bullet_points(
        list=[
            '🍎 Apple',
            '🍊 Orange',
            '🍐 Pear',
            '🥝 Kiwi',
            '🥭 Mango'
        ], title=title_builder.create_title('My favourite fruits'))

    numbers = bullet_point_builder.create_bullet_points(
        [num for num in range(2, 10, 2)])

    """We can give each list item its own colour"""
    fruits.elements[0].style.color_name = 'red'
    fruits.elements[1].style.color_name = 'orange'
    fruits.elements[2].style.color_name = 'green'
    fruits.elements[3].style.color_name = 'darkgreen'
    fruits.elements[4].style.color_name = 'orange'

    # Render to the terminal
    print(fruits.rendered())
    print('Numbers:')
    print(numbers.rendered())
