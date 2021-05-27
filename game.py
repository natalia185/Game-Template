import arcade


#Global constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MenuView(arcade.View):

    def __init__(self):
        super().__init__()


    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Menu', SCREEN_WIDTH/2, SCREEN_HEIGHT/1.1,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        pass

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()


def main():
    '''Main method'''
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.set_location(400, 150)
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()