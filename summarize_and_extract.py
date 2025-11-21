import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(system, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    with open("extracted.json", "r", encoding="utf-8") as f:
        text = json.load(f)["text"]

    summary_prompt = f"""
    Summarize this Act in 5–10 bullet points focusing on:
    - Purpose
    - Key definitions
    - Eligibility
    - Obligations
    - Enforcement
    TEXT:
    {text}
    """

    summary = call_llm("You summarize legislative acts.", summary_prompt)

    extract_prompt = f"""
    Extract these sections:

    - definitions
    - obligations
    - responsibilities
    - eligibility
    - payments
    - penalties
    - record_keeping

    Return ONLY JSON:
    {{
        "definitions": "",
        "obligations": "",
        "responsibilities": "",
        "eligibility": "",
        "payments": "",
        "penalties": "",
        "record_keeping": ""
    }}

    TEXT:
    {text}
    """

    structured = call_llm("You extract structured legal data.", extract_prompt)

    with open("act_structured.json", "w", encoding="utf-8") as f:
        f.write(structured)

    print("✔ Saved structured data to act_structured.json")
