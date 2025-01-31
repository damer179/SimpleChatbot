import os
import requests
from bs4 import BeautifulSoup
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
# import google.generativeai
import anthropic
import gradio as gr

# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")

# Connect to OpenAI, Anthropic and Google; comment out the Claude or Google lines if you're not using them

openai = OpenAI()

claude = anthropic.Anthropic()

# A generic system message - no more snarky adversarial AIs!

system_message = "You are a helpful and creative assistant"

# Let's wrap a call to GPT-4o-mini in a simple function

def message_gpt(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
      ]
    completion = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
    )
    return completion.choices[0].message.content

def shout(text):
    print(f"Shout has been called with input {text}")
    return text.upper()

# The simplicty of gradio. This might appear in "light mode" - I'll show you how to make this in dark mode later.

# And now - changing the function from "shout" to "message_gpt"

gr.Interface(fn=message_gpt, inputs="textbox", outputs="textbox", flagging_mode="never").launch(share=True)

# view = gr.Interface(
#     fn=message_gpt,
#     inputs=[gr.Textbox(label="Your message:", lines=6)],
#     outputs=[gr.Textbox(label="Response:", lines=8)],
#     flagging_mode="never"
# )
# view.launch()