try:
    import pyglet
except:
    import os

    os.system("pip install --upgrade pyglet")
    import pyglet

import pyglet.window.key as key

# 0 = water
# 1 = sand
# 2 = stone wall
# 3 = grass

# static variables
tileLength = 64
screenLength = 960
screenHeight = 540
tileTypes = ("water.gif", "sand.gif", "robot.gif")
tileImages = []

# dymanic variables
screen = pyglet.window.Window()
screen.set_size(screenLength, screenHeight)
screenMutationX = 0
screenMutationY = 0
speed = 5

# tile init
for tileType in tileTypes:
    tileImages.append(pyglet.resource.image(tileType))

# player init
playerImage = pyglet.resource.image("player.gif")


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0
        # directions:
        # right = 1
        # left = 2
        # up = 3
        # down = 4

    def move(self, direction):
        self.direction = direction

    def update(self):
        if not checkHitboxes(self.direction):
            return
        if self.direction == 1:
            self.x += speed
        elif self.direction == 2:
            self.x -= speed
        elif self.direction == 3:
            self.y += speed
        elif self.direction == 4:
            self.y -= speed
        elif self.direction == 0:
            self.direction = 0


player = Player(50, 50)

# map
gameMap = [
    #  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 15
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 17
]


# functions
def displayMap():
    y = 0
    for row in reversed(gameMap):
        x = 0
        if player.y - screenHeight < y * tileLength < player.y + screenHeight:
            for tile in row:
                if player.x - screenLength < x * tileLength < player.x + screenLength:
                    tileImages[tile].blit(x * tileLength - screenMutationX, y * tileLength - screenMutationY)
                x += 1
        y += 1


def drawPlayer():
    playerImage.blit(player.x - screenMutationX - tileLength / 2, player.y - screenMutationY - tileLength / 2)


def updateScreenMutation():
    global screenMutationX
    global screenMutationY
    xMax = len(gameMap[1]) * tileLength
    yMax = len(gameMap) * tileLength
    print(xMax, yMax)
    if player.x < screenLength / 2:
        screenMutationX = 0
    elif player.x < xMax - screenLength / 2:
        screenMutationX = player.x - screenLength / 2
    else:
        screenMutationX = xMax - screenLength

    if player.y < screenHeight / 2:
        screenMutationY = 0
    elif player.y < yMax - screenHeight / 2:
        screenMutationY = player.y - screenHeight / 2
    else:
        screenMutationY = yMax - screenHeight
    print(screenMutationX, screenMutationY)


def checkHitboxes(dir):
    if dir == 1:
        if player.x + speed > len(gameMap[1]) * tileLength:
            return False
    elif player.direction == 2:
        if player.x - speed < 0:
            return False
    elif player.direction == 3:
        if player.y + speed > len(gameMap) * tileLength:
            return False
    elif player.direction == 4:
        if player.y - speed < 0:
            return False
    return True


@screen.event
def on_draw():
    player.update()
    updateScreenMutation()
    displayMap()
    drawPlayer()


@screen.event
def on_key_press(symbol, modifier):
    if symbol == key.W:
        player.move(3)
    if symbol == key.S:
        player.move(4)
    if symbol == key.A:
        player.move(2)
    if symbol == key.D:
        player.move(1)


@screen.event
def on_key_release(symbol, modifier):
    if symbol == key.W:
        player.move(0)
    if symbol == key.S:
        player.move(0)
    if symbol == key.A:
        player.move(0)
    if symbol == key.D:
        player.move(0)


pyglet.app.run()
