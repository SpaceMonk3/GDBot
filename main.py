import discord
import os
import requests
import json

client = discord.Client()


def get_Quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def translate(content, src, trgt):
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = "{\r \"q\": \""+ content+"\",\r\"source\": \""+src+"\",\r\"target\": \""+trgt+"\"\r}"

    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': 'df4a57dc9fmsh216de335b6e30ddp13e12ejsn10985c96a3ed',
        'x-rapidapi-host': "deep-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    json_data = json.loads(response.text)
    text = "" + json_data['data']['translations']['translatedText'] + ""
    return (text)


def change_Prefix(prefix):
    #temp = bot_prefix
    #bot_prefix = prefix.replace(temp + 'cp-','')
    return (bot_prefix)


bot_prefix = ','


@client.event
async def on_ready():
    print('PyBot logged in!!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(bot_prefix + 'quote'):
        quote = get_Quote()
        await message.channel.send(quote)

    if message.content.startswith(bot_prefix + 'cp'):
        await message.channel.send('Enter the new bot command')
        change_Prefix(message)
        await message.channel.send('The bot\'s prefix is now ' + bot_prefix)

    if message.content.startswith(bot_prefix + 'tr '):
        src = message.content[4:6]
        trgt = message.content[7:9]
        content = message.content[10:len(message.content)]
        await message.channel.send('Command disabled by Dev. so users get mad.. haha loser - unless you\'re the dev')

			   



client.run('Nzk3OTA3MzM2MDk3NDMxNjA0.X_tTHQ.tWQYpjnp5uWyvP7kK0Us7Q7_WzE')

#important stuff

#'Command disabled by Dev. so users get mad.. haha loser - unless you\'re the dev'

#'Translated text: '+translate(content, src, trgt)



