import discord
import os
import requests
import json
#from boto.s3.connection import S3Connection
#from boto.s3.key import Key

client = discord.Client()

'''
s3 = S3Connection(os.environ['API_KEY'], os.environ['TOKEN'])
bucket = s3.create_bucket('gdb_bot_secrets')
k = Key(bucket)

file = open('config.json',"r")
config = json.loads(file.read())
file.close()
'''

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
        'x-rapidapi-key': os.environ['API_KEY'],
        'x-rapidapi-host': "deep-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    json_data = json.loads(response.text)
    text = "" + json_data['data']['translations']['translatedText'] + ""
    return (text)


@client.event
async def on_ready():
    print('PyBot logged in!!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(',quote'):
        quote = get_Quote()
        await message.channel.send(quote)


    if message.content.startswith(',tr '):
        src = message.content[4:6]
        trgt = message.content[7:9]
        content = message.content[10:len(message.content)]
        await message.channel.send('Translated text: '+translate(content, src, trgt))

			   

client.run(os.environ['TOKEN'])


