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
