#!/usr/bin/python3
# -*- coding: utf-8 -*-

import viVoicecloud as vv

vv.Login()
t = vv.tts()
def aiui_answer(q, vv, tts):
        a = vv.aiui(q)
        if a[0] != 4:
            if a[1] in ["openQA", "datetime", "weather", "calc", "baike", "poetry", "news"]:
                for i in a[3]:
                    tts.say(i)
            elif a[1] == "musicX":
                tts.say("暂时未添加音乐模块")
            else:
                tts.say("对不起，这个问题有点难，无对应结果")
        else:
            tts.say("对不起， 没有这样的问题，回答不了")

print("请输入问题， 输入exit退出\n===============")
while 1:
    q = input("问题:")
    print(q)
    if q == "exit":
    	break
    else:
    	aiui_answer(q, vv, t)

vv.Logout()
