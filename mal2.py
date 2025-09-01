import sys, pygame

pygame.init()

width, height = 400, 600
screen = pygame.display.set_mode((400, 600))

clock = pygame.time.Clock()
fps = 60

player_x = width//2
player_y = height//2
player_speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    screen.fill('#000000')
    pygame.draw.circle(screen, '#ff0000', (player_x, player_y), 30)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()
    