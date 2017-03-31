import sys, pygame
pygame.init()

ball_size = (16, 16)
size = width, height = 640, 480

start_pos = [(size[0] - ball_size[0]) / 2, (size[1] - ball_size[1]) / 2]
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect.left, ballrect.top = start_pos


def test():
  return "abc"

print test()

x = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: x = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: x = 0
            if event.key == pygame.K_q: sys.exit()

    if x == 1: pass

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
