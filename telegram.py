import requests

def sendtext(bot_message):
    bot_token = '1652027589:AAFI9n81uTBWYIGXhbcWnAxqzM7sGdG69Kc'
    bot_chatID = '-1001369981227'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    

