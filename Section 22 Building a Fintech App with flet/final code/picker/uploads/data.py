import os
import openai
from dotenv import load_dotenv

load_dotenv()

PAGE_BG_COLOR = "#FFFFFF"
LEFT_NAVBAR_BG_COLOR = "#050509"
DEFAULT_PROMPTS = [
                   ("Discuss pros and cons", "\nof renewable energy sources."),
                   ("Describe the structure", "\nof a typical animal cell."),
                   ("Compare and contrast", "\nmitosis and meiosis."),
                   ("Explain the importance", "\nof the Hubble Space Telescope.")
                ]
IMAGE_URL = "https://avatars.githubusercontent.com/u/100697141?s=400&u=1da94baf8f5828e1790cc12544e85c01cf0b19db&v=4"
CHATGPT_IMAGE_URL = "https://tse3.mm.bing.net/th?id=OIP.8SHG1OHrBwCvUV7i_xPGpAHaHa&pid=Api&P=0&w=300&h=30"

openai.api_key = os.environ.get("CHATGPT_API_KEY")

def make_query(content : str):
   completion = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages=[{"role":"user", "content": content}]
   )

   return completion

