from __future__ import division
import pygame, urllib2, json, pprint,time
from random import randint, random
from datetime import datetime, timedelta
from urllib2 import urlopen
from colorsys import hsv_to_rgb

# setup some useful stuff for display
pygame.init()
SECONDS_IN_A_DAY = 86400
time_height = 1000
time_width = 1000
size=[time_width, time_height]
screen=pygame.display.set_mode(size)
max_req=200

display_from_uts = datetime.now() - timedelta(3)
display_to_uts = datetime.now()
from_date = display_from_uts.date()
to_date = display_to_uts.date()
split_days = (to_date - from_date).days

def seconds_past_midnight(time):
    return time.hour*3600 + time.minute*60 + time.second

def timestamp_from_datetime(datetime):
    return str(int(time.mktime(datetime.utctimetuple())))

# define the colors we will use in rgb format
black = [  0,  0,  0]
width_of_bar = time_width/(split_days + 1)

class Track(object):
    
    def __init__(self, name = '', datetime = datetime.now()):
        rgb = hsv_to_rgb(random(), 1, 1)
        self.color = [i*255 for i in rgb]
        self.datetime = datetime

    def update(self, screen):
        time = self.datetime.time()
        date = self.datetime.date()
        time_past_origin = date - from_date 
        # x position is based on how many days you are past the origin
        x = width_of_bar*time_past_origin.days
        # y position is based on portion through the day
        y = int((seconds_past_midnight(time)/SECONDS_IN_A_DAY)*time_height)
        rect = pygame.Rect((x, y), (width_of_bar,0))
        pygame.draw.rect(screen, self.color, rect)


## The actual work is done here!
# open the api_detail file
f = open('api_details.txt')
api_key = f.readline()
secret = f.readline() 
f.close()

# get some information
user = 'poulter7'
response = urlopen('http://ws.audioscrobbler.com/2.0/?format=json&from=' +timestamp_from_datetime(display_from_uts) + 'to='+timestamp_from_datetime(display_to_uts)+'&limit='+str(max_req)+'&method=user.getrecenttracks&user=' + user +'&api_key='+api_key )
json_response = response.read()

# process the response
data = json.loads(json_response)
track_data = data['recenttracks']['track']
tracks = [Track(name = t['name'], datetime = datetime.fromtimestamp(float(t['date']['uts']))) for t in track_data]

###
# Now some visuals
###
for t in tracks:
    t.update(screen)
pygame.display.update()

pygame.quit()
