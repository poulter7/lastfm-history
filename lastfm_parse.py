import sys, time, pygame

pygame.init()
size=[1000, 1000]
center=[200, 500]
screen=pygame.display.set_mode(size)

# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]
font = pygame.font.Font(None, 25)
 
class Track(object):
    def __init__(self, color = red, name ='', size = 2, date = 0):
        self.color = color
        self.size = size
        self.angle = angle
        self.pos = pos
        self.offset = offset
        self.text = font.render(name, True, white)

    def update(self, screen):
        p = (self.pos[0]+center[0], self.pos[1]+center[1])
        pygame.draw.circle(screen, self.color, (int(p[0]), int(p[1])), self.size)
#        screen.blit(self.text, [i+5 for i in p])


tracks_sprites = []
def display_data():
    screen.fill(black)
    for t in tracks_sprites:
        t.update(screen)
    pygame.display.update()

#pygame.quit()
