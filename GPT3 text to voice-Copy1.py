#!/usr/bin/env python
# coding: utf-8

# In[2]:


import openai


# In[3]:


API_KEY= 'Your OpenAI API here'


# In[4]:


openai.api_key = API_KEY

prompt = "Outline some of the things you would teach someone new about connecting to the OPENAI API"


# In[5]:


completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024)


# In[6]:


import requests
def elevenlabs_voice(text, voice_ID):
    
    url = 'https://api.elevenlabs.io/v1/text-to-speech/%s'%voice_ID
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': 'Your ElevenLabs API here',
        'Content-Type': 'application/json'
    }
    data = {
        'text': text
    }

    response = requests.post(url, headers=headers, json=data)
    return response


# In[7]:


import json
prompt = "Write a goodbye note to a dear friend"
voice_ID = 'ErXwobaYiN019PkySvjV'
completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024)
print(completions.choices[0].text)
language = 'en'
eleven_response = elevenlabs_voice(text=completions.choices[0].text, voice_ID = voice_ID)
print(eleven_response)
with open('response.mp3', 'wb') as f:
   f.write(eleven_response.content)
import subprocess
subprocess.call(["afplay", "response.mp3"])
#myobj.save("test.mp3")
#return_code = subprocess.call(["afplay", "test.mp3"])


# In[ ]:




