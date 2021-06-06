import arcade

#Global constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class LevelView(arcade.View):
    '''
    Class representing the screen with the choice of difficulty level
    '''

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Wybierz poziom trudności', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.3,
                         arcade.color.YELLOW_ORANGE, font_size=30, anchor_x="center")