import arcade

# Global constants
SCALING = 0.3


def frame():
    '''
    Function creates a basic map outline.
    '''
    wall_list = arcade.SpriteList(use_spatial_hash=True)

    for y in [20, 560]:
        for x in range(48):
            x = 50 + x * 15
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [50, 755]:
        for y in range(35):
            y = 35 + y * 15
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    return wall_list

def level_1():
    '''
    Function create game map for level 1.
    '''
    wall_list = frame()

    for x in [115, 690]:
        for y in range(12):
            y = 80 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [115, 690]:
        for y in range(12):
            y = 330 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [145, 660]:
        for y in range(10):
            y = 110 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [145, 660]:
        for y in range(10):
            y = 330 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [220, 585]:
        for y in range(6):
            y = 170 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [220, 585]:
        for y in range(6):
            y = 330 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [80, 495]:
        for x in range(14):
            x = 130 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [80, 495]:
        for x in range(15):
            x = 470 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [110, 465]:
        for x in range(13):
            x = 145 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [110, 465]:
        for x in range(13):
            x = 470 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [245, 330]:
        for x in range(25):
            x = 220 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [170, 405]:
        for x in range(25):
            x = 220 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [245, 330]:
        for x in [130, 675]:
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [95, 480]:
        for x in [325, 470]:
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in range(7):
        x = 400
        y = 20 + 15 * y
        wall = arcade.Sprite("./images/block.png", SCALING)
        wall.position = (x, y)
        wall_list.append(wall)

    for y in range(7):
        x = 400
        y = 465 + 15 * y
        wall = arcade.Sprite("./images/block.png", SCALING)
        wall.position = (x, y)
        wall_list.append(wall)

    return wall_list


def level_2():
    '''
    Function create game map for level 2.
    '''
    wall_list = frame()

    for y in [245, 330]:
        for x in range(21):
            x = 255 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [215, 370]:
        for x in range(21):
            x = 255 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [255, 555]:
        for y in range(2):
            y = 215 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [255, 555]:
        for y in range(3):
            y = 330 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [115, 690]:
        for y in range(12):
            y = 80 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [115, 690]:
        for y in range(12):
            y = 330 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [80, 495]:
        for x in range(14):
            x = 130 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [80, 495]:
        for x in range(15):
            x = 470 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [185, 625]:
        for y in range(8):
            y = 330 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for x in [185, 625]:
        for y in range(7):
            y = 150 + 15 * y
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in [150, 435]:
        for x in range(30):
            x = 185 + 15 * x
            wall = arcade.Sprite("./images/block.png", SCALING)
            wall.position = (x, y)
            wall_list.append(wall)

    for y in range(5):
        x = 400
        y = 20 + 15 * y
        wall = arcade.Sprite("./images/block.png", SCALING)
        wall.position = (x, y)
        wall_list.append(wall)

    for y in range(5):
        x = 400
        y = 495 + 15 * y
        wall = arcade.Sprite("./images/block.png", SCALING)
        wall.position = (x, y)
        wall_list.append(wall)

    return wall_list
