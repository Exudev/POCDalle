# imports 
import os
import imageConverter
import openai
import json
from pathlib import Path

PROMPT = input("Tell me what u want 2 see: ")

DATA_DIR = Path.cwd()/ "data"
DATA_DIR.mkdir(exist_ok=True)
# set API key
openai.api_key = os.getenv("OPENAI_API_KEY") #gets your API key from the environment variable that you saved it to earlier, every time u close 
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size = "256x256", #The argument needs to be a string—either "256x256", "512x512", or "1024x1024".
    response_format="b64_json", #The API allows you to switch the response format from a URL to the Base64-encoded image data.
)
print(response["data"][0]["b64_json"][:50])
file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json" # You use the beginning of the prompt and the timestamp from the JSON response to create a unique file name.

with open(file_name, mode="w", encoding="utf-8") as file:

    json.dump(response, file)

imageConverter.Base64toPng(file_name)