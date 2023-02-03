
# coding: utf-8



import openai





API_KEY= 'Your OpenAI API here'





openai.api_key = API_KEY







completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024)





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





import json
prompt = input("Talk to me goose: ")
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







