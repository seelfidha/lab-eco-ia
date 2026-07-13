import json
import requests

from utils import get_system_prompt, get_user_prompt

OLLAMA_URL = 'http://localhost:11434/api/chat'


def create_operation_plan(
        question: str,
        summary: dict,
        model: str) -> dict:

    print('Operation plan creation phase')

    system_prompt = get_system_prompt()
    user_prompt = get_user_prompt(summary, question)
    payload = {
        "model": "qwen3:0.6b",
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            },
            {
                "role": "system",
                "content": system_prompt
            }
        ],
        "stream": False,
        'thinking': False,
        'format': 'json',
    }
    print('interacting with the model')
    response = requests.post(
        "http://localhost:11434/api/chat",
        json = payload,
        timeout=240
    )

    data = response.json()

    print('Check variable done: ',data.get("done"))
    print('Check variable done reason: ',data.get("done_reason"))

    content = data["message"]["content"]

    print('this is the content returned by the model: ', content)
    if is_json(content):
        loads = json.loads(content)
        print("Final json loads:", loads)
        return loads
    else:
        print('No content returned by the model')
        return dict()

def is_json(text):
    try:
        return json.loads(text)
    except (TypeError, json.JSONDecodeError):
        return False
