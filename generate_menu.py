import json
from openai import OpenAI
import os
from datetime import datetime

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

with open("family_profile.json") as f:
    family = json.load(f)

with open("menu_history.json") as f:
    history = json.load(f)

with open("prompt.txt") as f:
    prompt = f.read()

messages = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": f"Family:\n{json.dumps(family)}\n\nHistory:\n{json.dumps(history)}"}
]

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

output = response.choices[0].message.content

week_id = datetime.now().strftime("%Y-W%U")

with open(f"output_{week_id}.txt", "w") as f:
    f.write(output)

history.append({
    "week": week_id,
    "menu": output
})

with open("menu_history.json", "w") as f:
    json.dump(history, f, indent=2)

print(output)
