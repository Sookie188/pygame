from cgitb import text
import pygame
from sys import exit

# this has to be the first line of code
pygame.init()
# create window
screen = pygame.display.set_mode((384*3, 216*3))
# set title
pygame.display.set_caption('cool game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/InkbitThree.ttf', 50)

BLACK = (0, 0, 0)

# functions
def scale(image, scale):
    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (width*scale, height*scale))
    return image

def get_image(sheet, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey(color)
    return image

# back- and foreground
grass = scale(pygame.image.load('graphics/grass.png'), 3)
back_1 = scale(pygame.image.load('graphics/background/plx-1.png'), 3)
back_2 = scale(pygame.image.load('graphics/background/plx-2.png'), 3)
back_3 = scale(pygame.image.load('graphics/background/plx-3.png'), 3)
back_4 = scale(pygame.image.load('graphics/background/plx-4.png'), 3)
back_5 = scale(pygame.image.load('graphics/background/plx-5.png'), 3)

# texts
text_surf = test_font.render('dino run', True, (203, 67, 75))

#dino
dino_surf = get_image(pygame.image.load('graphics/red_dino.png').convert_alpha(), 24, 24, 6, BLACK)
dino_rect = dino_surf.get_rect(midbottom = (50, 552+24))

#slime
slime_surf = scale(pygame.image.load('graphics/just_one_slime.png').convert_alpha(), 5)
slime_rect = slime_surf.get_rect(midbottom = (1152, 552+12))
# game will run in this loop, so that the window will not close at the end of code
while True:
    for event in pygame.event.get():
        # QUIT is the X button :)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('down')

    screen.blit(back_1, (0, 0))
    screen.blit(back_2, (0, 0))
    screen.blit(back_3, (0, 0))
    screen.blit(back_4, (0, 0))
    screen.blit(back_5, (0, 0))
    screen.blit(grass, (0, 552))
    screen.blit(grass, (480, 552))
    screen.blit(grass, (960, 552))

    screen.blit(text_surf, (80, 0))

    # dino
    screen.blit(dino_surf, dino_rect)

    # slime
    slime_rect.x -= 20
    if slime_rect.right <= 0: slime_rect.left = 1152
    screen.blit(slime_surf, slime_rect)

    if dino_rect.colliderect(slime_rect):
        print('u dieded')

    mouse_pos = pygame.mouse.get_pos()
    if dino_rect.collidepoint((mouse_pos)):
        print('aaahhhhhh')

    # I should not think about this
    pygame.display.update()
    # something about framerates
    clock.tick(60)
