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

#snares
snare_no_lights_1 = pygame.image.load('snare/snare_no_lights_1.png')
snare_no_lights_2 = pygame.image.load('snare/snare_no_lights_2.png')
snare_no_lights_3 = pygame.image.load('snare/snare_no_lights_3.png')
snare_no_lights_4 = pygame.image.load('snare/snare_no_lights_4.png')

snare_lights_1 = pygame.image.load('snare/snare_lights_1.png')
snare_lights_2 = pygame.image.load('snare/snare_lights_2.png')
snare_lights_3 = pygame.image.load('snare/snare_lights_3.png')
snare_lights_4 = pygame.image.load('snare/snare_lights_4.png')

#quads
quads_no_lights_1 = pygame.image.load('quads/quads_no_lights_1.png')
quads_no_lights_2 = pygame.image.load('quads/quads_no_lights_2.png')
quads_no_lights_3 = pygame.image.load('quads/quads_no_lights_3.png')
quads_no_lights_4 = pygame.image.load('quads/quads_no_lights_4.png')

quads_lights_1 = pygame.image.load('quads/quads_lights_1.png')
quads_lights_2 = pygame.image.load('quads/quads_lights_2.png')
quads_lights_3 = pygame.image.load('quads/quads_lights_3.png')
quads_lights_4 = pygame.image.load('quads/quads_lights_4.png')

#cymbals
cymbals_down_1 = pygame.image.load('cymbals/cymbals_down_1.png')
cymbals_down_2 = pygame.image.load('cymbals/cymbals_down_2.png')
cymbals_down_3 = pygame.image.load('cymbals/cymbals_down_3.png')
cymbals_down_4 = pygame.image.load('cymbals/cymbals_down_4.png')

cymbals_up_1 = pygame.image.load('cymbals/cymbals_up_1.png')
cymbals_up_2 = pygame.image.load('cymbals/cymbals_up_2.png')
cymbals_up_3 = pygame.image.load('cymbals/cymbals_up_3.png')
cymbals_up_4 = pygame.image.load('cymbals/cymbals_up_4.png')


#bass 1
bass_1_no_lights_1 = pygame.image.load('basses/bass_1_no_lights_1.png')
bass_1_no_lights_2 = pygame.image.load('basses/bass_1_no_lights_2.png')
bass_1_no_lights_3= pygame.image.load('basses/bass_1_no_lights_3.png')
bass_1_no_lights_4 = pygame.image.load('basses/bass_1_no_lights_4.png')

bass_1_lights_1 = pygame.image.load('basses/bass_1_lights_1.png')
bass_1_lights_2 = pygame.image.load('basses/bass_1_lights_2.png')
bass_1_lights_3 = pygame.image.load('basses/bass_1_lights_3.png')
bass_1_lights_4 = pygame.image.load('basses/bass_1_lights_4.png')

#bass 2
bass_2_no_lights_1 = pygame.image.load('basses/bass_2_no_lights_1.png')
bass_2_no_lights_2 = pygame.image.load('basses/bass_2_no_lights_2.png')
bass_2_no_lights_3 = pygame.image.load('basses/bass_2_no_lights_3.png')
bass_2_no_lights_4 = pygame.image.load('basses/bass_2_no_lights_4.png')

bass_2_lights_1 = pygame.image.load('basses/bass_2_lights_1.png')
bass_2_lights_2 = pygame.image.load('basses/bass_2_lights_2.png')
bass_2_lights_3 = pygame.image.load('basses/bass_2_lights_3.png')
bass_2_lights_4 = pygame.image.load('basses/bass_2_lights_4.png')

#bass 3
bass_3_no_lights_1 = pygame.image.load('basses/bass_3_no_lights_1.png')
bass_3_no_lights_2 = pygame.image.load('basses/bass_3_no_lights_2.png')
bass_3_no_lights_3 = pygame.image.load('basses/bass_3_no_lights_3.png')
bass_3_no_lights_4 = pygame.image.load('basses/bass_3_no_lights_4.png')

bass_3_lights_1 = pygame.image.load('basses/bass_3_lights_1.png')
bass_3_lights_2 = pygame.image.load('basses/bass_3_lights_2.png')
bass_3_lights_3 = pygame.image.load('basses/bass_3_lights_3.png')
bass_3_lights_4 = pygame.image.load('basses/bass_3_lights_4.png')

#bass 4
bass_4_no_lights_1 = pygame.image.load('basses/bass_4_no_lights_1.png')
bass_4_no_lights_2 = pygame.image.load('basses/bass_4_no_lights_2.png')
bass_4_no_lights_3 = pygame.image.load('basses/bass_4_no_lights_3.png')
bass_4_no_lights_4 = pygame.image.load('basses/bass_4_no_lights_4.png')

bass_4_lights_1 = pygame.image.load('basses/bass_4_lights_1.png')
bass_4_lights_2 = pygame.image.load('basses/bass_4_lights_2.png')
bass_4_lights_3 = pygame.image.load('basses/bass_4_lights_3.png')
bass_4_lights_4 = pygame.image.load('basses/bass_4_lights_4.png')

#bass 5
bass_5_no_lights_1 = pygame.image.load('basses/bass_5_no_lights_1.png')
bass_5_no_lights_2 = pygame.image.load('basses/bass_5_no_lights_2.png')
bass_5_no_lights_3 = pygame.image.load('basses/bass_5_no_lights_3.png')
bass_5_no_lights_4 = pygame.image.load('basses/bass_5_no_lights_4.png')

bass_5_lights_1 = pygame.image.load('basses/bass_5_lights_1.png')
bass_5_lights_2 = pygame.image.load('basses/bass_5_lights_2.png')
bass_5_lights_3 = pygame.image.load('basses/bass_5_lights_3.png')
bass_5_lights_4 = pygame.image.load('basses/bass_5_lights_4.png')

marimba = pygame.image.load('pit/marimba.png')
xylo = pygame.image.load('pit/xylo.png')
vibes = pygame.image.load('pit/vibes.png')
chimes = pygame.image.load('pit/chimes.png')

snare_no_lights = [snare_no_lights_1, snare_no_lights_2, snare_no_lights_3, snare_no_lights_4]
snare_lights = [snare_lights_1, snare_lights_2, snare_lights_3, snare_lights_4]

quads_no_lights = [quads_no_lights_1, quads_no_lights_2, quads_no_lights_3, quads_no_lights_4]
quads_lights = [quads_lights_1, quads_lights_2, quads_lights_3, quads_lights_4]

cymbals_down = [cymbals_down_1, cymbals_down_2, cymbals_down_3, cymbals_down_4]
cymbals_up = [cymbals_up_1, cymbals_up_2, cymbals_up_3, cymbals_up_4]

bass_1_no_lights = [bass_1_no_lights_1, bass_1_no_lights_2, bass_1_no_lights_3, bass_1_no_lights_4]
bass_1_lights = [bass_1_lights_1, bass_1_lights_2, bass_1_lights_3, bass_1_lights_4]

bass_2_no_lights = [bass_2_no_lights_1, bass_2_no_lights_2, bass_2_no_lights_3, bass_2_no_lights_4]
bass_2_lights = [bass_2_lights_1, bass_2_lights_2, bass_2_lights_3, bass_2_lights_4]

bass_3_no_lights = [bass_3_no_lights_1, bass_3_no_lights_2, bass_3_no_lights_3, bass_3_no_lights_4]
bass_3_lights = [bass_3_lights_1, bass_3_lights_2, bass_3_lights_3, bass_3_lights_4]

bass_4_no_lights = [bass_4_no_lights_1, bass_4_no_lights_2, bass_4_no_lights_3, bass_4_no_lights_4]
bass_4_lights = [bass_4_lights_1, bass_4_lights_2, bass_4_lights_3, bass_4_lights_4]

bass_5_no_lights = [bass_5_no_lights_1, bass_5_no_lights_2, bass_5_no_lights_3, bass_5_no_lights_4]
bass_5_lights = [bass_5_lights_1, bass_5_lights_2, bass_5_lights_3, bass_5_lights_4] 

# Settings
def draw_background(x, y):
    pygame.draw.rect(screen, BLACK, [0, 0, 800, 240])
    pygame.draw.polygon(screen, DARK_GRAY, [[50, 240], [10, 530], [790, 530],[750, 240]])
    screen.blit(logo, [250, 50])

def draw_snares(x, y, frame):
    if lights_on == False:
        screen.blit(snare_no_lights[frame], (x, y))
        screen.blit(snare_no_lights[frame], (x+100, y))
        screen.blit(snare_no_lights[frame], (x+200, y))

    else:
        screen.blit(snare_lights[frame], (x, y))
        screen.blit(snare_lights[frame], (x+100, y))
        screen.blit(snare_lights[frame], (x+200, y))

def draw_quads(x, y, frame):
    if lights_on == False:
        screen.blit(quads_no_lights[frame], (x, y))
        screen.blit(quads_no_lights[frame], (x+100, y))
        screen.blit(quads_no_lights[frame], (x+200, y))
    else:
        screen.blit(quads_lights[frame], (x, y))
        screen.blit(quads_lights[frame], (x+100, y))
        screen.blit(quads_lights[frame], (x+200, y))

def draw_cymbals(x, y, frame):
    if cymbals_position == False:
        screen.blit(cymbals_down[frame], (x, y))
        screen.blit(cymbals_down[frame], (x+100, y))
        screen.blit(cymbals_down[frame], (x+200, y))
        screen.blit(cymbals_down[frame], (x+300, y))
        screen.blit(cymbals_down[frame], (x+400, y))
    else:
        screen.blit(cymbals_up[frame], (x, y))
        screen.blit(cymbals_up[frame], (x+100, y))
        screen.blit(cymbals_up[frame], (x+200, y))
        screen.blit(cymbals_up[frame], (x+300, y))
        screen.blit(cymbals_up[frame], (x+400, y))

        
def draw_bass_drums(x, y, frame):
    if lights_on == False:
        screen.blit(bass_1_no_lights[frame], (x, y))
        screen.blit(bass_2_no_lights[frame], (x+100, y))
        screen.blit(bass_3_no_lights[frame], (x+200, y))
        screen.blit(bass_4_no_lights[frame], (x+300, y))
        screen.blit(bass_5_no_lights[frame], (x+400, y))
    else:
        screen.blit(bass_1_lights[frame], (x, y))
        screen.blit(bass_2_lights[frame], (x+100, y))
        screen.blit(bass_3_lights[frame], (x+200, y))
        screen.blit(bass_4_lights[frame], (x+300, y))
        screen.blit(bass_5_lights[frame], (x+400, y))
        
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
cymbals_position = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lights_on = not lights_on
            elif event.key == pygame.K_c:
                cymbals_position = not cymbals_position
  

    # Game logic
    ticks += 1 
    if ticks%10 == 0:
        frame +=1
        if frame > 3:
            frame = 0  
    # Drawing code
    screen.fill(DARK_RED)
    draw_background(0, 0)
    draw_snares(400, 275, frame)
    draw_quads(100, 275, frame)
    draw_cymbals(150, 350, frame)
    draw_bass_drums(150, 200, frame)
    draw_pit(100, 500)

        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
