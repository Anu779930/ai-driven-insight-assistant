import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_insight(summary_text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a senior data analyst. Convert raw stats into clear business insights."
            },
            {"role": "user", "content": summary_text}
        ]
    )

    return response.choices[0].message.content