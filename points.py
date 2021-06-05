import arcade

# Global constants
SCALING = 0.5

def level_1():
    '''
    Function inserts points for the map from level 1.
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
        x = 112 + 36 * x
        y = 290
        point = arcade.Sprite("./images/point.png", SCALING)
        point.position = (x, y)
        points_list.append(point)

    return points_list
