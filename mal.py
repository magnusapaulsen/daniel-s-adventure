'''
Install Pygame
1. Open Terminal or Command Center
2. "pip install pygame"

Install VS Code
1. Google "vs code"
2. Follow download instructions
'''
# Get pieces of code for system and pygame
import sys, pygame

# Initialize pygame so we get access to the pieces of code
pygame.init()

# Create the game window
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mitt spill')

# Create the game clock
clock = pygame.time.Clock()

# Create the game loop
running = True # While this variable (boolean) is true, the game runs
while running:
    # Events - We check what the player inputs to the game
    for event in pygame.event.get(): # Check if player exits the game
        if event.type == pygame.QUIT:
            running = False
    
    # Updates - Movement, collisions, etc

    # Drawing - Updating the screen

    # We use pygame.draw to draw the shapes

    pygame.display.flip() # This updates the screen (double buffer, front/back)
    clock.tick(60) # The game updates at 60 frames per second

# When we exit the loop, the game ends and the program closes
pygame.quit()
sys.exit()






