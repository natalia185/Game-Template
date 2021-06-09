import arcade
import random
import math
import maps
import points


#Global constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'PACMAN'
SPRITE_SCALING = 0.5
PLAYER_MOVEMENT_SPEED = 5
ENEMY_MOVEMENT_SPEED = 1


def top(txt_file):
    '''
    Function takes data from a file and creates a list with the best results.
    '''
    score_list = []
    with open(txt_file, 'r') as file:
        for line in file:
            score = line.strip('\n')
            score_list.append(score)
        score_list.sort(reverse=True)
    return score_list


#Global constants - list with best scores
EASY_LEADER = top('best_easy.txt')
MEDIUM_LEADER = top('best_medium.txt')
HARD_LEADER = top('best_hard.txt')


class MenuView(arcade.View):
    '''
    Class representing the game menu screen.
    '''
    def __init__(self):
        super().__init__()
        self.logo = arcade.load_texture("./images/logo.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(300, 530, 200, 50, self.logo)
        arcade.draw_text('Menu', SCREEN_WIDTH/2, SCREEN_HEIGHT/1.3,
                         arcade.color.YELLOW_ORANGE, font_size=30, anchor_x="center")
        arcade.draw_text('Graj - naciśnij P', 370, SCREEN_HEIGHT / 1.5,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text('Instrukcja  - naciśnij I', 400, SCREEN_HEIGHT / 1.85,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text('Najlepsze wyniki - naciśnij N', 435, SCREEN_HEIGHT / 1.65,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text('O autorze - naciśnij A', 400, SCREEN_HEIGHT / 2.1,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text('ZAMKNIJ - esc', SCREEN_WIDTH / 2, 15,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.P:
            view = ModeView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)
        elif key == arcade.key.I:
            view = InstructionView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)
        elif key == arcade.key.N:
            view = BestScoreView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)
        elif key == arcade.key.ESCAPE:
            self.window.close()
        elif key == arcade.key.A:
            view = AuthorView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)


class ModeView(arcade.View):
    '''
    Class representing the screen with the choice of difficulty mode.
    '''
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Wybierz poziom trudności', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.3,
                         arcade.color.YELLOW_ORANGE, font_size=30, anchor_x="center")
        arcade.draw_text('ŁATWY - NACIŚNI L', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5,
                         arcade.color.YELLOW_ORANGE, font_size=25, anchor_x="center")
        arcade.draw_text('ŚREDNI - NACIŚNIJ S', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.7,
                         arcade.color.YELLOW_ORANGE, font_size=25, anchor_x="center")
        arcade.draw_text('TRUDNY - NACIŚNIJ T', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.YELLOW_ORANGE, font_size=25, anchor_x="center")
        arcade.draw_text("Aby wrócić do Menu wciśnij spację.", SCREEN_WIDTH / 2, 10,
                         arcade.color.YELLOW_ORANGE, font_size=15, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.L:
            view = GameView()
            view.user_mode = 1
            self.window.show_view(view)
            self.window.set_mouse_visible(False)
            view.setup()
        elif key == arcade.key.S:
            view = GameView()
            view.user_mode = 2
            self.window.show_view(view)
            self.window.set_mouse_visible(False)
            view.setup()
        elif key == arcade.key.T:
            view = GameView()
            view.user_mode = 3
            self.window.show_view(view)
            self.window.set_mouse_visible(False)
            view.setup()
        elif key == arcade.key.SPACE:
            view = MenuView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)


class Player(arcade.Sprite):
    '''
    Class represents player on screen.
    '''
    def update(self):
        '''
        Function sets appropriate ranges.
        '''
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.top > SCREEN_HEIGHT - 30:
            self.top = SCREEN_HEIGHT - 30
        elif self.bottom < 0:
            self.bottom = 0


class Enemy(arcade.Sprite):
    '''
    Class represents enemies on screen.
    '''
    def follow_sprite(self, player_sprite):
        '''
        The function will move the current sprite in the direction of
        another sprite that is given as a parameter.
        '''
        self.center_x += self.change_x
        self.center_y += self.change_y

        if random.randrange(0, 50) == 0:
            start_x = self.center_x
            start_y = self.center_y

            #Get the player location
            player_x = player_sprite.center_x
            player_y = player_sprite.center_y

            #Calculation the angle between the position of the player and the enemy
            x_diff = player_x - start_x
            y_diff = player_y - start_y
            angle = math.atan2(y_diff, x_diff)

            self.change_x = math.cos(angle) * ENEMY_MOVEMENT_SPEED
            self.change_y = math.sin(angle) * ENEMY_MOVEMENT_SPEED


class GameView(arcade.View):
    '''
    Class creating game and game view.
    '''
    def __init__(self):
        super().__init__()

        #Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.wall_list = None
        self.point_list = None

        #Motion control keys
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.player_sprite = None
        self.physics_engine = None
        self.score = 0
        self.level = 1

        #Player lives
        self.player_lives = 3
        self.player_live_image = None

        #Load sounds from https://mixkit.co/
        self.collect_points_sound = arcade.load_sound("./sounds/mixkit-game-ball-tap-2073.wav")
        self.kill_sound = arcade.load_sound("./sounds/mixkit-player-losing-or-failing-2042.wav")
        self.next_level_sound = arcade.load_sound("./sounds/mixkit-extra-bonus-in-a-video-game-2045.wav")

        #User choice level
        self.user_mode = 1

    def setup(self):
        '''
        Set up the game and initialize the variables.
        '''
        #Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.point_list = arcade.SpriteList(use_spatial_hash=True)

        #Set up walls and points
        if self.user_mode == 1:
            self.wall_list = maps.level_1()
            self.point_list = points.level_1()
        elif self.user_mode == 2:
            self.wall_list = maps.level_2()
            self.point_list = points.level_2()
        elif self.user_mode == 3:
            self.wall_list = maps.level_3()
            self.point_list = points.level_3()

        #Set up the player
        self.player_sprite = Player("./images/pacman.png", SPRITE_SCALING)
        self.player_sprite.position = (50, 290)
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        #Set up enemies
        enemy = Enemy('./images/pink.png', SPRITE_SCALING)
        enemy.position = (370, 70)
        self.enemy_list.append(enemy)

        enemy = Enemy('./images/blue.png', SPRITE_SCALING)
        enemy.position = (370, 530)
        self.enemy_list.append(enemy)

        enemy = Enemy('./images/red.png', SPRITE_SCALING)
        enemy.position = (720, 150)
        self.enemy_list.append(enemy)

        enemy = Enemy('./images/orange.png', SPRITE_SCALING)
        enemy.position = (720, 500)
        self.enemy_list.append(enemy)

        #Load player live
        self.player_live_image = arcade.load_texture("./images/pacman_live.png")

    def on_key_press(self, key, modifiers):
        '''
        Called when a key is pressed.
        '''
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        '''
        Called when the user releases a key.
        '''
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
        #Player movement
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

        #Enemies movement
        for enemy in self.enemy_list:
            enemy.follow_sprite(self.player_sprite)

        #Check collision between enemies and the player
        if arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list):
            arcade.play_sound(self.kill_sound)
            self.player_sprite.position = (50, 290)
            self.player_lives -= 1

        #End game and write scores
        if self.player_lives == 0:
            if self.user_mode == 1:
                if str(self.score) > EASY_LEADER[-1]:
                    with open('best_easy.txt', 'w') as file:
                        EASY_LEADER[-1] = str(self.score)
                        EASY_LEADER.sort(reverse=True)
                        new_score_list = [score + '\n' for score in EASY_LEADER]
                        file.writelines(new_score_list)
            elif self.user_mode == 2:
                if str(self.score) > MEDIUM_LEADER[-1]:
                    with open('best_medium.txt', 'w') as file:
                        MEDIUM_LEADER[-1] = str(self.score)
                        MEDIUM_LEADER.sort(reverse=True)
                        new_score_list = [score + '\n' for score in MEDIUM_LEADER]
                        file.writelines(new_score_list)
            elif self.user_mode == 3:
                if str(self.score) > HARD_LEADER[-1]:
                    with open('best_hard.txt', 'w') as file:
                        HARD_LEADER[-1] = str(self.score)
                        HARD_LEADER.sort(reverse=True)
                        new_score_list = [score + '\n' for score in HARD_LEADER]
                        file.writelines(new_score_list)

            arcade.play_sound(self.kill_sound)
            view = GameOverView(self)
            self.window.show_view(view)
            self.window.set_mouse_visible(True)

        #Enemies collision with walls
        for enemy in self.enemy_list:
            enemy.center_x += enemy.change_x
            walls_hit = arcade.check_for_collision_with_list(enemy, self.wall_list)
            for wall in walls_hit:
                if enemy.change_x > 0:
                    enemy.right = wall.left
                elif enemy.change_x < 0:
                    enemy.left = wall.right
            if len(walls_hit) > 0:
                enemy.change_x *= -1

            enemy.center_y += enemy.change_y
            walls_hit = arcade.check_for_collision_with_list(enemy, self.wall_list)
            for wall in walls_hit:
                if enemy.change_y > 0:
                    enemy.top = wall.bottom
                elif enemy.change_y < 0:
                    enemy.bottom = wall.top
            if len(walls_hit) > 0:
                enemy.change_y *= -1

        #Score update
        self.point_list.update()
        point_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.point_list)
        for point in point_hit_list:
            point.remove_from_sprite_lists()
            arcade.play_sound(self.collect_points_sound)
            self.score += 1

        #Change level
        self.point_list.update()
        if len(self.point_list) == 0:
            self.level += 1
            arcade.play_sound(self.next_level_sound)
            self.setup()

    def on_show(self):
        #Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.point_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()

        for y in range(self.player_lives):
            arcade.draw_lrwh_rectangle_textured(5, 15 + 30 * y, 30, 30, self.player_live_image)

        arcade.draw_text(f"Wynik: {self.score}", 10, 570, arcade.color.YELLOW_ORANGE, 18)
        arcade.draw_text(f"Poziom {self.level}", 360, 570, arcade.color.YELLOW_ORANGE, 18)


class GameOverView(arcade.View):
    '''
    Class representing the end game screen.
    '''
    def __init__(self, gameview):
        super().__init__()
        self.game_view = gameview

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Gra skończona", SCREEN_WIDTH / 2, SCREEN_HEIGHT/1.3,
                         arcade.color.YELLOW_ORANGE, font_size=40, anchor_x="center")
        arcade.draw_text(f"Twój wynik: {self.game_view.score}", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.45,
                         arcade.color.YELLOW_ORANGE, font_size=30, anchor_x="center")
        arcade.draw_text("Zagraj ponownie - naciśnij P", SCREEN_WIDTH / 2, 350,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text("Menu - naciśnij spację", SCREEN_WIDTH / 2, 310,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text('ZAMKNIJ - esc', SCREEN_WIDTH / 2, 15,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")


    def on_key_press(self, key, modifiers):
        if key == arcade.key.P:
            view = ModeView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)
        elif key == arcade.key.SPACE:
            view = MenuView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)
        elif key == arcade.key.ESCAPE:
            self.window.close()


class BestScoreView(arcade.View):
    '''
    Class representing a screen with a table of best results.
    '''
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Najlepsze wyniki", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.15,
                         arcade.color.YELLOW_ORANGE, font_size=40, anchor_x="center")
        arcade.draw_text("Aby wrócić do Menu wciśnij spację.", SCREEN_WIDTH / 2, 10,
                         arcade.color.YELLOW_ORANGE, font_size=15, anchor_x="center")

        #Draw tables
        arcade.draw_text('ŁATWY', 190, SCREEN_HEIGHT / 1.4,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text('ŚREDNI', 430, SCREEN_HEIGHT / 1.4,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text('TRUDNY', 680, SCREEN_HEIGHT / 1.4,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")

        arcade.draw_line(20, SCREEN_HEIGHT / 1.4, SCREEN_WIDTH - 20, SCREEN_HEIGHT / 1.4, arcade.color.YELLOW_ORANGE)
        arcade.draw_line(310, 100, 310, SCREEN_HEIGHT / 1.3, arcade.color.YELLOW_ORANGE)
        arcade.draw_line(560, 100, 560, SCREEN_HEIGHT / 1.3, arcade.color.YELLOW_ORANGE)
        arcade.draw_line(80, 100, 80, SCREEN_HEIGHT / 1.3, arcade.color.YELLOW_ORANGE)

        for index in range(1, 11):
            arcade.draw_text('%s.' % index, 60, 425 - 30 * index,
                             arcade.color.YELLOW_ORANGE, font_size=15, anchor_x="center")

        #Add scores
        with open('best_easy.txt') as file1, open('best_medium.txt') as file2, open('best_hard.txt') as file3:
            y = 0
            for line in file1:
                arcade.draw_text(line, 190, 380 - 30 * y, arcade.color.YELLOW_ORANGE, font_size=15, anchor_x="center")
                y += 1
            y = 0
            for line in file2:
                arcade.draw_text(line, 430, 380 - 30 * y, arcade.color.YELLOW_ORANGE, font_size=15, anchor_x="center")
                y += 1
            y = 0
            for line in file3:
                arcade.draw_text(line, 680, 380 - 30 * y, arcade.color.YELLOW_ORANGE, font_size=15, anchor_x="center")
                y += 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            view = MenuView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)


class InstructionView(arcade.View):
    '''
    Class representing the game instruction screen.
    '''
    def __init__(self):
        super().__init__()
        self.up_key = arcade.load_texture('./images/up_down.png')
        self.key_right = arcade.load_texture('./images/right_left.png')

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instrukcja gry", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.15,
                         arcade.color.YELLOW_ORANGE, font_size=40, anchor_x="center")
        arcade.draw_text("Celem gry jest zdobycie jak największej ilości punktów.\n"
                         "Punkty uzyskuje się poprzez pochłanianie Pacmanem \n"
                         "kulek rozmieszczonych na mapie. Przy czym ważne jest \n"
                         "unikanie wrogo nastawionych przeciwników, którymi są \n"
                         "Blinky, Pinky, Inky i Clyde.\n"
                         "Kontakt z choć jednym z nich oznacza utratę jednego życia.\n"
                         "W ciągu całej rozgrywki gracz ma do dyspozycji tylko 3 życia.\n"
                         "Do poruszania Pacmanem służą strzałki\n",
                         400, SCREEN_HEIGHT / 2.3,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x='center')
        arcade.draw_lrwh_rectangle_textured(100, 200, 30, 60, self.up_key)
        arcade.draw_text("- w górę", 190, 235,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text("- w dół", 185, 200,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_lrwh_rectangle_textured(400, 200, 30, 60, self.key_right)
        arcade.draw_text("- w prawo", 490, 235,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text("- w lewo", 485, 200,
                         arcade.color.YELLOW_ORANGE, font_size=20, anchor_x="center")
        arcade.draw_text("Aby wrócić do Menu wciśnij spację.", SCREEN_WIDTH / 2, 10,
                         arcade.color.YELLOW_ORANGE, font_size=15, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            view = MenuView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)


class AuthorView(arcade.View):
    '''
    Class representing a screen with information about the author.
    '''
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Kilka słów o autorze", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2,
                         arcade.color.YELLOW_ORANGE, font_size=40, anchor_x="center")
        arcade.draw_text("Cześć!\n"
                         "Mam na imię Natalia i jestem studentką Politechniki Wrocławskiej.\n"
                         "Niniejsza gra została napisana na potrzeby kursu z programowania\n"
                         "i jest moją wersją popularnej niegdyś gry arkadowej Pac-man.\n\n"
                         "Dlaczego akurat Pac-man? Była to jedna z pierwszych gier \n"
                         "w jakie grałam w dzieciństwie. Dlatego też kiedu usłyszałam \n"
                         "hasło 'gra arkadowa' to właśnie o tej grze od razu pomyślałam.\n\n"
                         "Mam nadzieję, że moja wersja gry się wam spodoba. Miłej zabawy :)",
                         SCREEN_WIDTH / 2, 260,
                         arcade.color.YELLOW_ORANGE, font_size=18, anchor_x="center")
        arcade.draw_text("Aby wrócić do Menu wciśnij spację.", SCREEN_WIDTH / 2, 10,
                         arcade.color.YELLOW_ORANGE, font_size=15, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            view = MenuView()
            self.window.show_view(view)
            self.window.set_mouse_visible(True)


def main():
    '''
    Function initializes games.
    '''
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.set_location(400, 150)
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()