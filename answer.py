def aiui_answer(q, vv, tts):
    a = vv.aiui(q)
    if a[0] != 4:
        if a[1] in ["openQA", "datatime", "weather", "calc", "bike", "poetry", "news"]:
            for i in a[3]:
                tts.say(i)

        elif a[1] == "musixX":
            tts.say("暂时未添加音乐模块")

        else:
            tts.say("对不起，这个问题有点难，无对应结果")
    else:
        tts.say("对不起， 没有这样的问题，回答不了")
myga = {
        "你好":"你好！跟我聊聊吧",
        "你真聪明":"没人生来杰出",
        "再见":"勇敢地前进吧朋友"
        }

def my_answer(q, tts):
    for key in myqa:
        if key in myqa:
            tts.say(myqa[key])
            return value
        else:
            return False
        
if __name__ == "__main__":
    import viVoicecloud as vv
    vv.Login()
    tts.vv.tts()
    q = input("问题:")
    my_answer(q, tts)
    vv.Logout()