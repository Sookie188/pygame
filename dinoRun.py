import pygame


def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = test_font.render(f'{current_time}', False, (203, 67, 75))
    score_rect = score_surf.get_rect(center=(screen_width/2, 50))
    screen.blit(score_surf, score_rect)


# this has to be the first line of code
pygame.init()
# create window
screen_width = 384*2
screen_height = 216*2
screen = pygame.display.set_mode((screen_width, screen_height))
# set title
pygame.display.set_caption('Dino Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/InkbitThree.ttf', 50)
game_active = True

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
grass = scale(pygame.image.load('graphics/grass.png'), 2)
back_1 = scale(pygame.image.load('graphics/background/plx-1.png'), 2)
back_2 = scale(pygame.image.load('graphics/background/plx-2.png'), 2)
back_3 = scale(pygame.image.load('graphics/background/plx-3.png'), 2)
back_4 = scale(pygame.image.load('graphics/background/plx-4.png'), 2)
back_5 = scale(pygame.image.load('graphics/background/plx-5.png'), 2)

# dino
dino_surf = get_image(pygame.image.load(
    'graphics/red_dino.png').convert_alpha(), 24, 24, 4, BLACK)
dino_rect = dino_surf.get_rect(midbottom=(
    100, screen_height-grass.get_height()+24))
player_gravity = 0

# slime
slime_surf = scale(pygame.image.load(
    'graphics/just_one_slime.png').convert_alpha(), 3)
slime_rect = slime_surf.get_rect(midbottom=(
    screen_width, screen_height-grass.get_height()+12))

# game will run in this loop, so that the window will not close at the end of code
while True:
    for event in pygame.event.get():
        # QUIT is the X button :)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dino_rect.bottom >= screen_height-grass.get_height()+24:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN and dino_rect.bottom >= screen_height-grass.get_height()+24:
                if dino_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                slime_rect.left = screen_width

    if game_active:
        screen.blit(back_1, (0, 0))
        screen.blit(back_2, (0, 0))
        screen.blit(back_3, (0, 0))
        screen.blit(back_4, (0, 0))
        screen.blit(back_5, (0, 0))
        screen.blit(grass, (0, screen_height-grass.get_height()))
        screen.blit(grass, (grass.get_width(),
                    screen_height-grass.get_height()))
        screen.blit(grass, (grass.get_width()*2,
                    screen_height-grass.get_height()))

        # scoreboard
        display_score()

        # dino
        player_gravity += 1
        dino_rect.y += player_gravity
        if dino_rect.bottom >= screen_height-grass.get_height()+24:
            dino_rect.bottom = screen_height-grass.get_height()+24
        screen.blit(dino_surf, dino_rect)

        # slime
        slime_rect.x -= 5
        if slime_rect.right <= 0:
            slime_rect.left = screen_width
        screen.blit(slime_surf, slime_rect)

        # collision
        if slime_rect.colliderect(dino_rect):
            game_active = False
    else:
        screen.fill('Darkred')

    # I should not think about this
    pygame.display.update()
    # something about framerates
    clock.tick(60)
