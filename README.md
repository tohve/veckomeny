# 🧠 Weekly Menu Agent

A simple AI-powered family meal planner that generates weekly dinner plans every Friday.

---

## ✨ What it does

Every Friday the agent:
- Generates 5 dinners (Mon–Fri)
- Respects your family preferences
- Balances fish, meat, vegetarian meals
- Creates shopping list
- Includes a simple prep plan
- Avoids repeating recent meals

---

## 👨‍👩‍👧‍👦 Family rules (built-in)

- 4 people
- Fish: 1–2 times/week
- Soup: 1 time/week
- 1 meal/week cooked from scratch project
- Max 45 min weekday cooking
- Always vegetarian option for Person 2
- No coriander for Person 1
- Person 2: no beef, pork, chicken, lamb (pescatarian)

---

## 📁 Project structure

```
family_profile.json   → your preferences
menu_history.json    → memory of past weeks
prompt.txt           → AI instructions
generate_menu.py     → main generator
.github/workflows/   → scheduled execution
```

---

## 🚀 Setup

### 1. Install dependencies
```bash
pip install openai
```

### 2. Add API key (GitHub Secrets)
Add:
```
OPENAI_API_KEY
```

### 3. Push to GitHub
Then enable GitHub Actions.

---

## ⏰ Schedule

Runs automatically:
```
Every Friday at 18:00 CET
```

You can also trigger manually from GitHub Actions.

---

## 🧠 How it works

1. Loads family profile
2. Loads previous menus
3. Sends everything to OpenAI
4. Generates weekly plan
5. Saves output + updates memory

---

## 📌 Output includes

- Weekly dinner plan
- Shopping list
- Prep instructions
- Seasonal suggestions

---

## 🔧 Next improvements (recommended)

- Send email automatically (M365 / Gmail)
- Add feedback loop (👍 👎 responses)
- Seasonal Swedish ingredient intelligence
- Avoid repetition smarter than last-8-weeks filter

---

## 💡 Philosophy

> “Don’t find one meal everyone loves — design a system of variations.”

