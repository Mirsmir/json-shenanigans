import urllib.request
import requests
import json
import random

for i in range(20):
    url = 'https://apimeme.com/meme?meme=Albert-Einstein-1&top=Top+text&bottom=Bottom+text'
    response = urllib.request.urlopen(url)

    topText = ["cold+pizza", "skibidi+rizz", "stunned silence", "always+enough+poop", "poop+gun"]
    bottomText = ["always+rizzy", "from+ohio", "deadly", "never+enough+time", "epic"]

    top = random.choice(topText)
    bot = random.choice(bottomText)
    memeNames = ["Albert Einstein 1", "Angry Birds Pig", "Alan Greenspan", "Alarm Clock", "Advice Doge"]

    memeName = random.choice(memeNames)

    r = response.get(url,allow_redirects=True)
    open(f'{i}-picture_meme.jpg', 'wb').write(r.content)
    print("meme configured")

