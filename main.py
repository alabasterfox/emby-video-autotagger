import csv
import requests

'''
Emby Video Autotagger
Quickly tag library videos via Emby's API
Written on Python v3.8.10 for Emby v4.7.5.0
'''

def add_tag(video_id, tagtext):
    media_server_url = 'emby-server-address-goes-here'    # <== update this before use
    api_key = 'api-key-goes-here'                         # <== update this before use

    # format request
    uri = "http://{}/emby/Items/{}/Tags/Add?api_key={}".format(media_server_url, video_id, api_key)
    json = { 'Tags': [{ 'Name': tagtext, 'Id': '0' }]}

    # send request to media server
    response = requests.post(uri, json = json)
    print(response)

if __name__ == "__main__":
    video_id_tags_mapping = dict()
    video_ids = []

    '''
    # just example data - update as needed
    video_ids.append('1')
    video_ids.append('2')
    video_id_tags_mapping['1'] = "action|critically-acclaimed"
    video_id_tags_mapping['2'] = "adventure|comedy|cult-classic"
    '''

    for video_id in video_ids:
        if video_id in video_id_tags_mapping:
            id = video_id
            tags = video_id_tags_mapping[video_id]
            for tag in tags.split("|"):
                # commit tag
                add_tag(id, tag)

''' 
Q: What and where are the video IDs?
A: Emby v4.7.5.0 creates a unique id to reference each video in its library. This
ID metadata is stored in a SQLite database named 'library.db' in a table named 
'MediaItems'. When installed on top of Ubuntu, this db can be located at the path 
/var/lib/emby/data/library.db.  Or you can locate it by running a command like: 
terminal> sudo find / -name "library.db"

'''