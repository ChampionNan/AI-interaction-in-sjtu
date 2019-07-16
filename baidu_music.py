#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:32:03 2019

@author: apple
"""

import urllib, json, vlc, time
import urllib.request

url = "http://tingapi.ting.baidu.com/v1/restserver/ting?"
url += "from=webapp_misic"
url += "&method=baidu.ting.search.catalogSug"
url += "&format=json"

keywords = "五月天 温柔"
keywords_encoded = urllib.parse.quote(keywords)
#print("keywords_encoded:",keywords_encoded)

url += "&query="+keywords_encoded

ref = urllib.request.urlopen(url)

result = ref.read()
#print("Result:",result)

json_str1 = str(result, encoding = 'utf-8')
dict1 = json.loads(json_str1)
songid = dict1["song"][0]["songid"]
#print(songid)

url2 = "http://music.taihe.com/data/music/fmlink?"
url2 += "songIds="+songid
    
ref2 = urllib.request.urlopen(url2)
result2 = ref2.read()
#print("result2:",result2)

dic2 = json.loads(str(result2, encoding = 'utf-8'))
#print("ok:",dic2)
songLink = dic2['data']['songList'][0]['songLink']
#print("Link:",songLink)

p = vlc.MediaPlayer(songLink)
p.play()
time.sleep(2)
while p.is_playing():
    time.sleep(0.5)
p.stop()
p.release()
