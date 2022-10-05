import pygame

pygame.init()
win = pygame.display.set_mode((500, 450))

pygame.display.set_caption('Игра началась')

walkright = [
    pygame.image.load('images/frame-1.png'),
    pygame.image.load('images/frame-2.png'),
    pygame.image.load('images/frame-3.png'),
    pygame.image.load('images/frame-4.png'),
    pygame.image.load('images/frame-5.png'),
    pygame.image.load('images/frame-6.png'),
    pygame.image.load('images/frame-7.png'),
    pygame.image.load('images/frame-8.png'),
]

walkleft = [
    pygame.image.load('images/frame-1.png'),
    pygame.image.load('images/frame-2.png'),
    pygame.image.load('images/frame-3.png'),
    pygame.image.load('images/frame-4.png'),
    pygame.image.load('images/frame-5.png'),
    pygame.image.load('images/frame-6.png'),
    pygame.image.load('images/frame-7.png'),
    pygame.image.load('images/frame-8.png'),
]

playerStand = pygame.image.load('images/frame-1.png')

bg = pygame.image.load('images/les.png')

clock = pygame.time.Clock()
x = 10
y = 320
r = 40
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

lastmove = "right"

class snar():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
       
def dw():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 40:
        animCount = 0
    if left:
        win.blit(walkleft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkright[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


run = True
bullets = []
while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastmove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 3:
            bullets.append(snar(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastmove = "left"
    elif keys[pygame.K_RIGHT] and x < 450 - 5:
        x += speed
        left = False
        right = True
        lastmove = "right"

    else:
        left = False
        right = False
        animCount = 0

    if not isJump:
        if keys[pygame.K_UP] and y - r > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < 450 - r - 5:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= jumpCount * 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    dw()

pygame.quit()
