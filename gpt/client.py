import openai
from config import settings

openai.api_key = settings.openai_api_key


def generate_text(prompt: str) -> str:
    if not openai.api_key:
        raise RuntimeError("OPENAI_API_KEY not configured")

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    )
    return response.choices[0].message.content
