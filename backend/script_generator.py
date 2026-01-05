import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Groq API configuration (Free and Fast)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def generate_script(topic):
    with open("prompts/script_prompt.txt", "r") as f:
        prompt = f.read().format(topic=topic)

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are an expert educational content creator who writes engaging video scripts."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        raise Exception(f"Groq API error: {str(e)}. Get free API key at https://console.groq.com")


if __name__ == "__main__":
    topic = "How WebSockets work"
    script = generate_script(topic)
    print(script)
