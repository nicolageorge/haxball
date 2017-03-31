import sys, pygame, time, random

pygame.init()

ball_size = (16, 16)
size = width, height = 640, 480

start_pos = [(size[0] - ball_size[0]) / 2, (size[1] - ball_size[1]) / 2]
speed = [1, 1]
speed2 = [6, 6]
black = 0, 0, 0

delay = float(sys.argv[1] or 2)
start_pos[0] = int(sys.argv[2] or start_pos[0])
start_pos[1] = int(sys.argv[3] or start_pos[1])

print start_pos

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect.left, ballrect.top = start_pos

screen.fill(black)
screen.blit(ball, ballrect)
pygame.display.flip()

time.sleep(delay)

# def save_pos():
#     ballrect[0]

# print test()

x = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: x = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: x = 0


    if x == 1: continue

    t = random.random() > 0.5
    ballrect = ballrect.move(speed if t else speed2)
    if ballrect.left <= ball_size[0] or ballrect.right >= width - ball_size[0]:
        speed[0], speed2[0] = -speed[0],  -speed2[0]
    if ballrect.top <= ball_size[1] or ballrect.bottom >= height - ball_size[1]:
        speed[1], speed2[1] = -speed[1], -speed2[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
