import pygame, urllib2, json, datetime, pprint

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
        self.size = 3

    def update(self, screen):
        p = (0,0)
        pygame.draw.circle(screen, self.color, p, self.size)



###
# Get a list of some tracks
###
# open the api_detail file
f = open('api_details.txt')
api_key = f.readline()
secret = f.readline() 
f.close()

# get some information
user = 'poulter7'
from_uts = str(0)
to_uts = str(0)
response = urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?format=json&from=' +from_uts + 'to='+to_uts+'&method=user.getrecenttracks&user=' + user +'&api_key='+api_key )
json_response = response.read()

# process the response
data = json.loads(json_response)
track_data = data['recenttracks']['track']

###
# Now some visuals
###
ts = datetime.datetime.fromtimestamp
tracks = [Track(name = t['name'], date = ts(float(t['date']['uts']))) for t in track_data]

def display_data():
    screen.fill(black)
    for t in tracks:
        t.update(screen)
    pygame.display.update()

pygame.quit()
