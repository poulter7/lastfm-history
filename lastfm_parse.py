import sys, time, pygame, urllib2, json, pprint

# open the api_detail file
f = open('api_details.txt')
api_key = f.readline()
secret = f.readline() 
f.close()

# get some information
user = 'poulter7'
response = urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?format=json&method=user.getrecenttracks&user=' + user +'&api_key='+api_key )
json_response = response.read()

# process the response
data = json.loads(json_response)
tracks = ['recenttracks']['track']

# setup some useful stuff for display
pygame.init()
size=[1000, 1000]
screen=pygame.display.set_mode(size)

# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]
font = pygame.font.Font(None, 25)

class Track(object):
    def __init__(self, color = red, name = '', date = 0):
        self.color = color
        self.date = date
        self.text = font.render(name, True, white)

    def update(self, screen):
        p = (0,0)
        pygame.draw.circle(screen, self.color, p, self.size)
        screen.blit(self.text, p)


tracks_sprites = []
def display_data():
    screen.fill(black)
    for t in tracks_sprites:
        t.update(screen)
    pygame.display.update()

pygame.quit()
