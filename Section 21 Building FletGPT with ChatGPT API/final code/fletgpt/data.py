import os
import openai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("CHATGPT_API_KEY")

# setting openai api key
openai.api_key = API_KEY

# connecting with chatgpt api

def chatgpt_response(content):
   response = openai.ChatCompletion.create(
      model= "gpt-3.5-turbo",
      messages = [{"role": "user", "content": content }],
      temperature = 0.7
   )

   return response["choices"][0]["message"]["content"]


PAGE_BG_COLOR = "#FFFFFF"
DEFAULT_PROMPTS = [
                   ("Discuss pros and cons", "\nof renewable energy sources."),
                   ("Describe the structure", "\nof a typical animal cell."),
                   ("Compare and contrast", "\nmitosis and meiosis."),
                   ("Explain the importance", "\nof the Hubble Space Telescope.")
                ]

CHATGPT_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/1200px-ChatGPT_logo.svg.png"
IMAGE_URL = "https://avatars.githubusercontent.com/u/100697141?s=400&u=1da94baf8f5828e1790cc12544e85c01cf0b19db&v=4"

# openai
