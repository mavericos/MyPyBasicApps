import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Jumper')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 80)
game_active = True

sky_surface = pygame.image.load('Earth.jpg').convert()

score_surf = test_font.render(' Jumper ', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 50))

alien_surf = pygame.image.load('alien.png').convert_alpha()
alien_rect = alien_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('monster.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 260))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        if event.type == pygame.MOUSEBUTTONDOWN:
          if player_rect.collidepoint(event.pos) and player_rect >= 350:
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 350:
                player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
    if game_active:
        screen.blit(sky_surface,(-50,-100))
        pygame.draw.rect(screen,'#c0e8ec', score_rect)
        pygame.draw.rect(screen,'#c0e8ec', score_rect, 10)
        screen.blit(score_surf,score_rect)

        alien_rect.x -= 2
        if alien_rect.right <= 0: alien_rect.left = 800
        screen.blit(alien_surf,alien_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 350: player_rect.bottom = 350
        screen.blit(player_surf, player_rect)

        # collision
        if alien_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('green')

    pygame.display.update()
    clock.tick(60)

    # https: // www.youtube.com / watch?v = AY9MnQ4x3zk
    # 1:54:40

