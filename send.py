import requests


def sendmessage(api, chatid, text):
    requests.get(
        "https://api.telegram.org/bot{}/sendMessage?chat_id={}>&text={}"
            .format(api, chatid, text))
