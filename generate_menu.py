import json
from openai import OpenAI
import os
from datetime import datetime

# Initiera OpenAI-klienten
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Läs in familjeprofil
with open("family_profile.json", encoding="utf-8") as f:
    family = json.load(f)

# Läs in historik
with open("menu_history.json", encoding="utf-8") as f:
    history = json.load(f)

# Läs in prompt
with open("prompt.txt", encoding="utf-8") as f:
    prompt = f.read()

# Bygg meddelanden till modellen
messages = [
    {
        "role": "system",
        "content": (
            prompt
            + "\n\nAll output must be in Swedish. "
              "Skriv alltid menyer, inköpslistor och instruktioner på svenska."
        )
    },
    {
        "role": "user",
        "content": (
            f"Familjeprofil:\n{json.dumps(family, ensure_ascii=False, indent=2)}\n\n"
            f"Historik:\n{json.dumps(history, ensure_ascii=False, indent=2)}"
        )
    }
]

# Anropa modellen
try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.7,
        max_tokens=2000
    )
except Exception as e:
    print("Fel vid API-anrop:", e)
    exit(1)

# Hämta och säkra output
output = response.choices[0].message.content
output = output.encode("utf-8", "replace").decode()

# Skapa svensk ISO-vecka
week_id = datetime.now().strftime("%G-W%V")

# Spara veckans meny
output_filename = f"output_{week_id}.txt"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(output)

# Uppdatera historiken
history.append({
    "week": week_id,
    "menu": output
})

with open("menu_history.json", "w", encoding="utf-8") as f:
    json.dump(history, f, indent=2, ensure_ascii=False)

print(f"Veckomeny genererad och sparad i {output_filename}")
