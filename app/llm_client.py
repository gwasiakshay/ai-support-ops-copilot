import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "AI Support Ops Copilot",
}


def call_llm(prompt: str):
    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are an AI assistant for post-sales support operations.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }

    response = requests.post(
        f"{OPENROUTER_BASE_URL}/chat/completions",
        headers=HEADERS,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
