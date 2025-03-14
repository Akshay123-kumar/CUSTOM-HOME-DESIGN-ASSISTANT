import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("AIzaSyBV_VcW7qu8YVew0BIVRNLB3p96E-4h2L8")

# Configure Generative AI
genai.configure(api_key=API_KEY)

# Function to generate home design ideas
def generate_design_idea(style, size, rooms):
    return f"The design for a {style} home of {size} with {rooms} rooms includes modern layouts and materials."
