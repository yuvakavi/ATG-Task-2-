import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Groq API configuration (Free and Fast)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def generate_blueprint(script):
    with open("prompts/blueprint_prompt.txt", "r") as f:
        prompt = f.read().format(script=script)

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are an expert animator who creates detailed animation blueprints for educational videos."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 800
    }
    
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        raise Exception(f"Groq API error: {str(e)}. Get free API key at https://console.groq.com")


if __name__ == "__main__":
    sample_script = "Client sends request to server..."
    blueprint = generate_blueprint(sample_script)
    print(blueprint)
