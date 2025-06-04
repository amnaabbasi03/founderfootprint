# summarize.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary_report(name, articles):
    combined_text = "\n\n".join([a['text'] for a in articles])[:12000]  # Limit input size

    prompt = f"""
You are an expert research assistant. Analyze the following content about {name} and generate a structured summary with these sections:

1. Background
2. Recent News
3. Achievements
4. Controversies
5. Public Sentiment
6. Notable Quotes

Only include information found in the text. Be concise and factual. Avoid speculation.

Articles:
{combined_text}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful analyst summarizing media content about a startup founder or CEO."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )

    output = response.choices[0].message.content

    # Optional: split sections into a dictionary
    sections = {}
    current_section = ""
    for line in output.splitlines():
        if line.strip().startswith(tuple("123456")):
            parts = line.split(".", 1)
            if len(parts) == 2:
                current_section = parts[1].strip()
                sections[current_section] = ""
        elif current_section:
            sections[current_section] += line.strip() + "\n"

    return sections

