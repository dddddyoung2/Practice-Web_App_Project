import spotipy
import requests
import urllib.request
import pandas as pd
import jinja2
import json
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

cid = '1f92ddc6d6d540e9b78ec8a08222b81a'
secret = '92ba299f48be46a2bb089cc99ec0a137'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#api = spotipy.oauth2.API

def get_tracks(self, _id):
    try:
        raw_user = sp.get_tracks(_id)
    except:
        return None
    return raw_user


# def get_artist(self, _id):
#     return self.get_resource(_id, resource_type='artists')