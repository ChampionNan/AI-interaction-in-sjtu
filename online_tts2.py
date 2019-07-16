#!/usr/bin/python3
# -*- coding: utf-8 -*-

import viVoicecloud as vv

vv.Login()

t = vv.tts()

t.SessionBegin(voice = "nannan", speed = 7, volume = 10)

t.TextPut(text = "你好啊")

t.AudioGet(filepath = "aaa.wav")

t.SessionEnd()

vv.Logout()
