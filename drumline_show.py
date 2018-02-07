# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Rainy Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (100, 125, 75)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (200, 200, 100)
BLACK = (0, 0, 0)
DARK_RED = (90, 32, 32)

# Images
logo = pygame.image.load('CWEA.png')

snare_no_lights_1 = pygame.image.load('snare/snare_no_lights_1.png')
snare_no_lights_2 = pygame.image.load('snare/snare_no_lights_2.png')
snare_no_lights_3 = pygame.image.load('snare/snare_no_lights_3.png')
snare_no_lights_4 = pygame.image.load('snare/snare_no_lights_4.png')

snare_lights_1 = pygame.image.load('snare/snare_lights_1.png')
snare_lights_2 = pygame.image.load('snare/snare_lights_2.png')
snare_lights_3 = pygame.image.load('snare/snare_lights_3.png')
snare_lights_4 = pygame.image.load('snare/snare_lights_4.png')

quads_no_lights_1 = pygame.image.load('quads/quads_no_lights_1.png')
quads_no_lights_2 = pygame.image.load('quads/quads_no_lights_2.png')
quads_no_lights_3 = pygame.image.load('quads/quads_no_lights_3.png')
quads_no_lights_4 = pygame.image.load('quads/quads_no_lights_4.png')

quads_lights_1 = pygame.image.load('quads/quads_lights_1.png')
quads_lights_2 = pygame.image.load('quads/quads_lights_2.png')
quads_lights_3 = pygame.image.load('quads/quads_lights_3.png')
quads_lights_4 = pygame.image.load('quads/quads_lights_4.png')

marimba = pygame.image.load('pit/marimba.png')
xylo = pygame.image.load('pit/xylo.png')
vibes = pygame.image.load('pit/vibes.png')
chimes = pygame.image.load('pit/chimes.png')

snare_no_lights = [snare_no_lights_1, snare_no_lights_2, snare_no_lights_3, snare_no_lights_4]
snare_lights = [snare_lights_1, snare_lights_2, snare_lights_3, snare_lights_4]
quads_no_lights = [quads_no_lights_1, quads_no_lights_2, quads_no_lights_3, quads_no_lights_4]
quads_lights = [quads_lights_1, quads_lights_2, quads_lights_3, quads_lights_4]

# Settings
def draw_logo(x, y):
    screen.blit(logo, [x, y])

def draw_snare(x, y, frame):
    if lights_on == False:
        screen.blit(snare_no_lights[frame], (x, y))
    else:
        screen.blit(snare_lights[frame], (x, y))

def draw_quads(x, y, frame):
    if lights_on == False:
        screen.blit(quads_no_lights[frame], (x, y))
    else:
        screen.blit(quads_lights[frame], (x, y))

def draw_pit(x, y):
    screen.blit(chimes, (x, y))
    screen.blit(xylo, (x+75, y))
    screen.blit(xylo, (x+150, y))
    screen.blit(marimba, (x+250, y))
    screen.blit(marimba, (x+350, y))
    screen.blit(vibes, (x+450, y))
    screen.blit(vibes, (x+525, y))


# Game loop
done = False
ticks = 0
frame = 0
lights_on = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lights_on = not lights_on
  

    # Game logic
    ticks += 1 
    if ticks%10 == 0:
        frame +=1
        if frame > 3:
            frame = 0  
    # Drawing code
    screen.fill(DARK_RED)
    pygame.draw.rect(screen, BLACK, [0, 0, 800, 240])
    pygame.draw.polygon(screen, DARK_GRAY, [[100, 240], [60, 480], [740, 480],[700, 240]])
    draw_logo(250, 50)
    draw_snare(600, 300, frame)
    draw_snare(500, 300, frame)
    draw_snare(400, 300, frame)
    draw_quads(300, 300, frame)
    draw_quads(200, 300, frame)
    draw_quads(100, 300, frame)
    draw_pit(100, 450)

        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
