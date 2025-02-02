import sys, pygame
from tank import Tank
from bullet import Bullet

pygame.init()

size = width, height = 1800, 900
speed = [1, 0]
tank_width, tank_height = 80, 80
grey = 112, 112, 112
i = 0

screen = pygame.display.set_mode(size)
screen_rect = screen.get_rect()

clock = pygame.time.Clock()
timer_interval = 500
next_bullet_time = 500
next1_bullet_time = 500

tank_image = pygame.image.load("tank.png").convert_alpha()
tank_destroyed_image = pygame.image.load("tank_destroyed.png").convert_alpha()
tank = Tank(tank_image, tank_destroyed_image,  speed=5, x=0, y=0)

tank1_image = pygame.image.load("tank1.png").convert_alpha()
tank1_destroyed_image = pygame.image.load("tank1_destroyed.png").convert_alpha()
tank1 = Tank(tank1_image, tank1_destroyed_image, speed=5, x=width-73, y=height-80)

bimg = pygame.image.load("bullet.png")


# tank2_image = pygame.image.load("tank2.png").convert_alpha()
# tank2 = Tank(tank2_image, speed=5, x=0, y=height-80)
#
# tank3_image = pygame.image.load("tank3.png").convert_alpha()
# tank3 = Tank(tank3_image, speed=5, x=width-73, y=0)

tank_bullets = pygame.sprite.Group()
tank1_bullets = pygame.sprite.Group()


space_pressed = 0
space1_pressed = 0
while True:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(grey)
    tank.check_ifout(screen_rect)
    tank1.check_ifout(screen_rect)
    tank_bullets.draw(screen)
    tank1_bullets.draw(screen)

    if space1_pressed == 1:
        tank1_bullets.update()

    if space_pressed == 1:
        tank_bullets.update()


    keys = pygame.key.get_pressed()
    start_time = pygame.time.get_ticks()


    if tank1.turn == 4 or tank1.turn == -4: #one cicle
        tank1.turn = 0;

    if (tank1.speed != 0):
        if keys[pygame.K_UP]:
            tank1.move(up=True)

        if keys[pygame.K_DOWN]:
            tank1.move(down=True)
        if keys[pygame.K_LEFT]:
            tank1.move(turn_left=True)
        if keys[pygame.K_RIGHT]:
            tank1.move(turn_right=True)

    if tank.turn == 4 or tank.turn == -4: #one cicle
        tank.turn = 0;

    if (tank.speed != 0):
        if keys[pygame.K_w]:
            tank.move(up=True)

        if keys[pygame.K_s]:
            tank.move(down=True)
        if keys[pygame.K_a]:
            tank.move(turn_left=True)
        if keys[pygame.K_d]:
            tank.move(turn_right=True)



    current_time = pygame.time.get_ticks()
    if current_time > next1_bullet_time:
        if keys[pygame.K_SPACE]:
            tank1_bullets.add(Bullet(bimg, tank1))
            space1_pressed = 1;
        next1_bullet_time += timer_interval

    for tank1_bullet in tank1_bullets:
        if tank1_bullet.rect.colliderect(tank.rect):
            tank.speed = 0
            tank.image = tank.destroyed_image
            tank.rect.x = tank.rect.x - 16
            tank.rect.y = tank.rect.y - 16

    current_time = pygame.time.get_ticks()
    if current_time > next_bullet_time:
        if keys[pygame.K_f]:
            tank_bullets.add(Bullet(bimg, tank))
            space_pressed = 1;
        next_bullet_time += timer_interval

    for tank_bullet in tank_bullets:
        if tank_bullet.rect.colliderect(tank1.rect):
            tank1.speed = 0
            tank1.image = tank1.destroyed_image
            tank1.rect.x = tank1.rect.x - 16
            tank1.rect.y = tank1.rect.y - 16



    # screen.blit(tank.image, tank.rect)
    screen.blit(tank.image, tank.rect)
    screen.blit(tank1.image, tank1.rect)



    # screen.blit(tank2.image, tank2.rect)
    # screen.blit(tank3.image, tank3.rect)
    clock.tick(100)
    pygame.display.flip()
