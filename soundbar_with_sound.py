import pygame
from load_and_parse_sound import load_song
import numpy as np
import sounddevice as sd

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FRAME_RATE = 20
N_SOUNDBAR = 40
FILENAME = "test.mp3"
STEREO = True
TOP_N_FREQUENCIES = 200
NORMALISATION_VALUE = 3

BLUE = (0, 0, 255)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 500])

# represents a frequency bucket with its amplitude, a blue bar on the surface 
class SoundBar():
    def __init__(self,x,y):
        self.bar = pygame.Rect(x,y,10,0)
        self.amplitude = []#samples per second 

soundbars = []
data, fs, blocks = load_song(FILENAME,STEREO,FRAME_RATE,N_SOUNDBAR,TOP_N_FREQUENCIES,NORMALISATION_VALUE)
soundbar_range = np.linspace(20,990,N_SOUNDBAR)
#set position
for i in soundbar_range:
    sb = SoundBar(i,300)
    soundbars.append(SoundBar(i,300))

#set amplitude   
for sb_index in range(len(soundbars)):
    for b in blocks:
        soundbars[sb_index].amplitude.append(b[1][sb_index])

# Setup the clock for a decent framerate, 
# amount of changes in amplitude in a second per frequency
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True

t=0
#play the song
sd.play(data, fs)
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    for sb in soundbars:
        sb.bar.height = sb.amplitude[t] 
        sb.bar.topleft = (sb.bar.topleft[0],300-sb.amplitude[t])
        pygame.draw.rect(screen, BLUE, sb.bar)
    t+=1
    pygame.display.flip()
    # Ensure program maintains a rate of FRAMERATE per second
    clock.tick(FRAME_RATE)

# Done! Time to quit.
pygame.quit()