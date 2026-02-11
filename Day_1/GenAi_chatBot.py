import requests
import json
import os

API_KEY = os.environ.get("OPENROUTER_API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

while True:
    msg = input("You: ")

    if msg.lower() == "bye":
        print("AI: Bye! Have a great day!")
        break

    payload = {
        "model": "openai/gpt-4o-mini",   # FIX 1: valid model
        "messages": [
            {"role": "user", "content": msg}
        ]
    }

    r = requests.post(URL, headers=headers, json=payload)

    # FIX 2: check HTTP status
    if r.status_code != 200:
        print("HTTP Error:", r.status_code)
        print(r.text)
        continue

    result = r.json()

    # FIX 3: check API-level error
    if "error" in result:
        print("API Error:", result["error"]["message"])
        continue

    # SAFE access
    print("AI:", result["choices"][0]["message"]["content"])
