import json


def safe_json_parse(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON returned by model", "raw_output": text}
