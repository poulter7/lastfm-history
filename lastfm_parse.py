from __future__ import division
import pygame, urllib2, json, pprint
from random import randint, random
from datetime import datetime
from urllib2 import urlopen
from colorsys import hsv_to_rgb

# setup some useful stuff for display
pygame.init()
SECONDS_IN_A_DAY = 86400
time_height = 1000
time_width = 1000
size=[1000, 1000]
screen=pygame.display.set_mode(size)
font = pygame.font.Font(None, 25)

def seconds_past_midnight(time):
    return time.hour*3600 + time.minute*60 + time.second

# define the colors we will use in rgb format
black = [  0,  0,  0]
white = [255,255,255]                                                              
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

class Track(object):
    def __init__(self, name = '', datetime = datetime.now()):
        rgb = hsv_to_rgb(random(), 1, 1)
        self.color = [i*255 for i in rgb]
        self.datetime = datetime
        self.size = 1

    def update(self, screen):
        time = self.datetime.time()
        date = self.datetime.date()
        x = 100
        # y position is based on portion through the day
        y = int((seconds_past_midnight(time)/SECONDS_IN_A_DAY)*time_height)
        p = (x, y)
        print p
        print self.color
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
response = urlopen('http://ws.audioscrobbler.com/2.0/?format=json&from=' +from_uts + 'to='+to_uts+'&method=user.getrecenttracks&user=' + user +'&api_key='+api_key )
json_response = response.read()

# process the response
data = json.loads(json_response)
track_data = data['recenttracks']['track']

###
# Now some visuals
###
ts = datetime.fromtimestamp
tracks = [Track(name = t['name'], datetime = ts(float(t['date']['uts']))) for t in track_data]

def display_data():
    screen.fill(black)
    for t in tracks:
        t.update(screen)
    pygame.display.update()

display_data()
pygame.quit()
