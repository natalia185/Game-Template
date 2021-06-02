import arcade

# Global constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITILE = 'PACMAN'
SPRITE_SCALING = 0.3
PLAYER_MOVEMENT_SPEED = 5


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.logo = arcade.load_texture("./images/logo.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(300, 530, 200, 50, self.logo)
        arcade.draw_text('Menu', SCREEN_WIDTH/2, SCREEN_HEIGHT/1.3,
                         arcade.color.YELLOW_ORANGE, font_size = 30, anchor_x = "center")

    def on_mouse_press(self, x, y, button, modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
        self.window.set_mouse_visible(False)


class Player(arcade.Sprite):

    def update(self):
        #Checks and sets boundaries
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.top > SCREEN_HEIGHT - 30:
            self.top = SCREEN_HEIGHT - 30
        elif self.bottom < 0:
            self.bottom = 0


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.wall_list = None
        self.point_list = None

        # Motion control keys
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.physics_engine = None

    def setup(self):
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.point_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player
        self.player_sprite = Player("./images/pacman.png", SPRITE_SCALING)
        self.player_sprite.position = (40, 50)
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        # Player movement
        self.physics_engine.update()

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = - PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = - PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        self.player_list.update()

    def on_show(self):
        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.wall_list.draw()
        self.point_list.draw()


def main():
    '''Main method'''
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITILE)
    window.set_location(400, 150)
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()