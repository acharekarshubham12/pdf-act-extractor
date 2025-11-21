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
    act = json.load(open("act_structured.json", "r", encoding="utf-8"))

    rules_text = """
    Check the Act for:

    1. Defines key terms
    2. Specifies eligibility
    3. Specifies authority responsibilities
    4. Includes enforcement or penalties
    5. Includes payments/entitlements
    6. Includes record-keeping/reporting

    Return ONLY JSON.
    """

    prompt = f"Act data:\n{json.dumps(act, indent=4)}\n\nRules:\n{rules_text}"

    result = call_llm("You perform rule-based legislative checks.", prompt)

    with open("final_report.json", "w", encoding="utf-8") as f:
        f.write(result)

    print("✔ Final report saved to final_report.json")
