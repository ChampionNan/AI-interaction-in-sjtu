#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:47:56 2019

@author: apple
"""
import viVoicecloud as vv

def aiui_answer(q, vv, tts):
    a = vv.aiui(q)
    if a[0] != 4:
        if a[1] in ["openQA", "datatime", "weather", "calc", "bike", "poetry", "news"]:
            for i in a[3]:
                tts.say(i)

        elif a[1] == "musicX":
            tts.say("暂时未添加音乐模块")

        else:
            tts.say("对不起，这个问题有点难，无对应结果")
    else:
        tts.say("对不起， 没有这样的问题，回答不了")

myqa = {
        "你好":"你好！跟我聊聊吧",
        "你真聪明":"没人生来杰出",
        "再见":"勇敢地前进吧朋友"
        }

def my_answer(q, tts):
    for key in myqa:
        if key in q:
            tts.say(myqa[key])
            return True
    return False
vv.Login()
t = vv.tts()
print("请输入问题,输入exit退出\n================")

while(1):
    try:
        q = input("问题:")
        if(my_answer(q, t)):
            print("my_answer")
        elif(q == "exit"):
            break
        else:
            aiui_answer(q,vv,t)
    except Exception as e:
        print(e)
        print('stopped')
        vv.Logout()
        break
