from cgitb import text
import pygame
from sys import exit

# this has to be the first line of code
pygame.init()
# create window
screen = pygame.display.set_mode((384, 216))
# set title
pygame.display.set_caption('cool game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/InkbitThree.ttf', 50)

back_1 = pygame.image.load('graphics/background/plx-1.png')
back_2 = pygame.image.load('graphics/background/plx-2.png')
back_3 = pygame.image.load('graphics/background/plx-3.png')
back_4 = pygame.image.load('graphics/background/plx-4.png')
back_5 = pygame.image.load('graphics/background/plx-5.png')
grass = pygame.image.load('graphics/grass.png')
text_surface = test_font.render('dino run', True, (203, 67, 75))

dino_sheet = pygame.image.load('graphics/red_dino.png').convert_alpha()
slime = pygame.image.load('graphics/just_one_slime.png')
bigger_slime = pygame.transform.scale(slime, (16*2, 12*2))
slime_x_pos = 384


def get_image(sheet, width, height, scale):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    return image


frame_0 = get_image(dino_sheet, 24, 24, 2.5)

# game will run in this loop, so that the window will not close at the end of code
while True:
    for event in pygame.event.get():
        # QUIT is the X button :)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(back_1, (0, 0))
    screen.blit(back_2, (0, 0))
    screen.blit(back_3, (0, 0))
    screen.blit(back_4, (0, 0))
    screen.blit(back_5, (0, 0))
    screen.blit(grass, (0, 216-31))
    screen.blit(grass, (160, 216-31))
    screen.blit(grass, (320, 216-31))
    # dino
    screen.blit(frame_0, (0, 145))

    # slime
    slime_x_pos -= 2
    if slime_x_pos < -100:
        slime_x_pos = 384
    screen.blit(bigger_slime, (slime_x_pos, 170))
    screen.blit(text_surface, (80, 0))

    # I should not think about this
    pygame.display.update()
    # something about framerates
    clock.tick(60)
