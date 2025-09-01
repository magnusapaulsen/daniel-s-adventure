import sys, pygame

pygame.init() # Initializes Pygame

# Creating game states
game_state = False

# Creating game window
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
game_name = "DANIEL'S ADVENTURE"
pygame.display.set_caption(game_name)
icon = pygame.image.load("daniel_icon.png")
pygame.display.set_icon(icon)

# Creating game clock
clock = pygame.time.Clock()
fps = 60
start_time = 0

# Creating font
font = pygame.font.Font(None, 50)

# Loading in background images
sky = pygame.image.load("sky.png").convert()
ground = pygame.image.load("ground.png").convert()

# Player settings
player = pygame.transform.scale((pygame.image.load("daniel_pose.png").convert_alpha()), (64,64*3))
player_rect = player.get_rect(midbottom = (100, 450))
player_intro = pygame.transform.scale((pygame.image.load("daniel_face.png").convert_alpha()), (256,256))
player_intro_rect = player_intro.get_rect(center = (width//2, height//2))
player_gravity = 0
player_speed = 5
player_jump_force = -25

# Snail settings
snail = pygame.image.load("snail.png").convert_alpha()
snail_starting_x = 600
snail_speed = 5
snail_rect = snail.get_rect(midbottom = (snail_starting_x, 450))

# Gravity settings
g = 0.271828 * 5

# Score
def DisplayScore():
    current_time = pygame.time.get_ticks()
    score_surface = font.render(str((current_time - start_time)//1000), False, ("#ffffff"))
    score_rect = score_surface.get_rect(center = (265, 300))
    screen.blit(score_surface, score_rect)
    # High score?

# Restart
restart_text_surface = font.render('Press "SPACE" to restart', False, ("#ffffff"))
restart_text_rect = restart_text_surface.get_rect(center = (width//2, height * 0.8))
                                                  
restart_title_surface = font.render(game_name, False, ("#ffffff"))
restart_title_rect = restart_title_surface.get_rect(center = (width//2, height//6))

# Enemy spawning
spawn_enemy = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_enemy, 500)


# Game loop
while True:
    # Exiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Check for jumping/restart input
        if event.type == pygame.KEYDOWN:
            if game_state == True:
                if event.key == pygame.K_SPACE and player_rect.bottom == 450:
                    player_gravity = -25
            else:
                if event.key == pygame.K_SPACE:
                    player_rect.midbottom = (100, 450)
                    snail_rect.midbottom = (snail_starting_x, 450)
                    score = 0
                    start_time = pygame.time.get_ticks()
                    game_state = True
                
        if event.type == spawn_enemy and game_state:
            print("spawning")

    if game_state:

        # Player movement
        if pygame.key.get_pressed()[pygame.K_a]:
            player_rect.x -= player_speed
        elif pygame.key.get_pressed()[pygame.K_d]:
            player_rect.x += player_speed
        player_rect.left -= player_speed // 2
        player_gravity += g
        player_rect.bottom += player_gravity

        # Clamp player movement
        if player_rect.left < 0:
            player_rect.left = 0
        elif player_rect.right > width:
            player_rect.right = width
        if player_rect.bottom > 450:
            player_rect.bottom = 450

        # Clamp snail movement and move snail
        if snail_rect.right < 0:
            snail_rect.left = snail_starting_x
            score += 1
        else:
            snail_rect.x -= snail_speed

        # Collisions
        if player_rect.colliderect(snail_rect):
            print("Game Over")
            game_state = False

        # Animations
        if player_rect.bottom < 425:
            player = pygame.transform.scale((pygame.image.load("daniel_laying.png").convert_alpha()), (192,64))
        elif player_rect.bottom >= 425:
            player = pygame.transform.scale((pygame.image.load("daniel_pose.png").convert_alpha()), (64,192))




        # Drawing
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 450))
        DisplayScore()
        screen.blit(snail, snail_rect)
        screen.blit(player, player_rect)

    else:
        screen.fill("#a9cfd6")
        screen.blit(player_intro, player_intro_rect)
        screen.blit(restart_text_surface, restart_text_rect)
        screen.blit(restart_title_surface, restart_title_rect)
    
    pygame.display.update()
    clock.tick(fps)