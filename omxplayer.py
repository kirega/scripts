#!/usr/bin/env python3

# import watchdog
import logging
import requests
import json
import pprint
from time import sleep
import sh
import itertools
# URL = 'http://35.190.176.112'
URL='http://localhost:8000'
class Scheduler(object):
    """
        A scheduler class to control what goes next into the  display.
    """

    def __init__(self, key):
        logging.debug("Scheduler initializing")
        self.next = ''
        # self.playlist = self.fetch_playlist()
        self.key = key
        self.asset = self.fetch_playlist()

    def fetch_playlist(self):
        logging.debug("Fetching the playlist")
        q = requests.get( URL + '/adverts/playlist',
                         headers={'Authorization': 'Token ' + self.key})
        q = q.content.decode('utf-8')
        q = json.loads(q)
        return self.fetch_assets(q)

    def fetch_assets(self,playlist):
        decoded_playlist = []
        for each in playlist:
            if len(each['adverts']) > 0:
                ads = ','.join(map(str,each['adverts']))
                r = requests.get( URL+'/adverts/list/?id__in='+ads, headers={'Authorization':'Token ' + self.key})
                r = r.content.decode('utf-8')
                r = json.loads(r)
                decoded_playlist.append(r)
        # print(decoded_playlist)
        decoded_playlist=list(itertools.chain.from_iterable(decoded_playlist))
        return decoded_playlist
    def get_call(self,url):
        r = requests.get(url, headers={'Authorization': ' Token ' + self.key})
        r = r.content.decode('utf-8')
        r = json.load(r)
        return r

def auth(user, pwd):
    r = requests.post(URL+'/rest_auth/login/',
                      data={'username': user, 'password': pwd})
    r = r.content.decode('utf-8')
    r = json.loads(r)
    return r['key']
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def play_video(uri, duration):
    print('Displaying video %s for %s', uri, duration)
    player_args = ['mpv',uri]
    # player_args = ['omxplayer', "--win '0 0  640 480'",uri]
    # player_kwargs = {'o': settings['audio_output'], '_bg': True, '_ok_code': [0, 124, 143]}
    if duration and duration != 'N/A':
        # ?print(duration)
      
        # player_args = ['timeout', 5 ] + player_args

        # player_args = ['timeout', get_sec(duration)] + player_args

        print(player_args)
    
    run = sh.Command(player_args[0])(*player_args[1:])
    while run.process.alive:
        # watchdog()
        print('hello')
        sleep(1)
    # if run.exit_code == 124:
    #     logging.error('player timed out')
    # except sh.ErrorReturnCode_1:
    #     logging.warning(
    #         'Resource URI is not correct, remote host is not responding or request was rejected')


def loop(scheduler):
    assets = scheduler.asset
    asset_generator = itertools.cycle(assets)
    current_asset = next(asset_generator)
    # print(current_asset['duration'])
    if 'video' in current_asset['type']:
        play_video(current_asset['upload'],current_asset['duration'])
    else:
        logging.warning('Unknown mime type')
    

if __name__ == "__main__":
    key = auth('kirega', 'mtotomdogo')

    global scheduler
    scheduler = Scheduler(key)
    while True:
        loop(scheduler)
