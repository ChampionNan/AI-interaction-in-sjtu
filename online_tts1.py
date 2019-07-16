#!/usr/bin/python3
# -*- coding: utf-8 -*-

import viVoicecloud as vv

vv.Login()

t = vv.tts()

t.say(text = "你好啊", voice = "nannan")

vv.Logout()