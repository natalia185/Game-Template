import arcade

# Global constants
SCALING = 0.5

def level_1():
    '''
    Function inserts points for the map from easy mode.
    '''
    points_list = arcade.SpriteList(use_spatial_hash=True)
    for x in [80, 725]:
        for y in range(17):
            y = 50 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [185, 617]:
        for y in range(10):
            y = 140 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [365, 435]:
        for y in range(2):
            y = 80 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [365, 435]:
        for y in range(3):
            y = 435 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [50, 530]:
        for x in range(8):
            x = 120 + 35 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [50, 530]:
        for x in range(8):
            x = 435 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [140, 435]:
        for x in range(13):
            x = 185 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in range(18):
        x = 113 + 36 * x
        y = 290
        point = arcade.Sprite("./images/point.png", SCALING)
        point.position = (x, y)
        points_list.append(point)

    return points_list


def level_2():
    '''
    Function inserts points for the map from medium mode.
    '''
    points_list = arcade.SpriteList(use_spatial_hash=True)
    for x in [80, 725]:
        for y in range(17):
            y = 50 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [150, 655]:
        for y in range(13):
            y = 110 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [222, 583]:
        for y in range(7):
            y = 185 + 35 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in range(18):
        x = 114 + 36 * x
        y = 290
        point = arcade.Sprite("./images/point.png", SCALING)
        point.position = (x, y)
        points_list.append(point)

    for x in [365, 435]:
        for y in [80, 500]:
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [50, 530]:
        for x in range(8):
            x = 120 + 35 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [50, 530]:
        for x in range(8):
            x = 435 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [110, 470]:
        for x in range(13):
            x = 184 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [185, 395]:
        for x in range(9):
            x = 260 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    return points_list


def level_3():
    '''
    Function inserts points for the map from hard mode.
    '''
    points_list = arcade.SpriteList(use_spatial_hash=True)
    for x in [80, 725]:
        for y in range(17):
            y = 50 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [150, 222, 583, 655]:
        for y in range(9):
            y = 150 + 35 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [365, 435]:
        for y in range(2):
            y = 80 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [365, 435]:
        for y in range(2):
            y = 465 + 30 * y
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for x in [115, 690]:
        y = 290
        point = arcade.Sprite("./images/point.png", SCALING)
        point.position = (x, y)
        points_list.append(point)

    for x in [296, 512]:
        for y in [220, 365]:
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [50, 530]:
        for x in range(8):
            x = 120 + 35 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [50, 530]:
        for x in range(8):
            x = 435 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [110, 465]:
        for x in range(6):
            x = 150 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [110, 465]:
        for x in range(6):
            x = 475 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [255, 325]:
        for x in range(9):
            x = 260 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    for y in [185, 400]:
        for x in range(7):
            x = 296 + 36 * x
            point = arcade.Sprite("./images/point.png", SCALING)
            point.position = (x, y)
            points_list.append(point)

    return points_list
