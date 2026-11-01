# Robo-Advisor Guide, Week 14 — The Advisor as a Skill

Tuesday of Week 14, self-paced: a guide and readings — no lab, no lecture, no checkout, no grade
item. What you build can seed your capstone.

**What you build:** a `client-letter` skill for your Week 13 `robo_app.py` that writes the
client's letter from the app's printed numbers only — and an app that flags any number it did not
print.

Design after matvix90/ai-robo-advisor (MIT). Data: Ken French Data Library; FRED, Federal Reserve Bank of St. Louis. Education, not investment advice.

## Readings

- [Lab 18](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/lab-18-legend-investor-as-skill.md)
  — the pattern: the skill lives where your AI reads skills; the numbers stay in code; the words
  are the model's; the app flags any number it did not print.
- Your AI's skills page: [Antigravity](https://antigravity.google/docs/skills) ·
  [Codex](https://developers.openai.com/codex/skills).
- [Week 13](../week-13/README.md) — your app, its data sources and its known answer.

## Your request

> Add a skill to my robo-advisor: `client-letter`, where my AI reads skills, with a name and a description that says when to use it.
>
> 1. `robo_app.py` saves the numbers it printed for the client on each run; the skill reads those and nothing else.
> 2. The skill writes the client's letter in plain words, saved as a `.md` file: the recommendation (stocks/bonds/cash); the rule behind it; the worst 12 months in percent and in dollars on the initial investment; whether that fits the client's maximum acceptable loss; and what would change the recommendation. If no stock/bond mix passes, the letter says so and claims no fit.
> 3. `robo_app.py` shows the letter and flags every number in it that the app did not print.
> 4. Keep the footer: "Design after matvix90/ai-robo-advisor (MIT). Data: Ken French Data Library; FRED, Federal Reserve Bank of St. Louis. Education, not investment advice."

Something not working? Debug with your AI: paste the exact command and the exact error text.

## Known answer

A client whose max loss is 25%, $100,000, the allocation overridden to 60/40/0. *Expect* the
letter to say: 60/40/0 and your rule; worst 12 months −24.41%, −$24,415 (the 12 months to February
2009); it fits the 25% max loss; and what would change the recommendation. *Expect* no flag. The
app's largest stock share within this client's max loss: 60%.

## Probes

1. **Max loss from 25% to 15%.** *Expect:* the app says no stock/bond mix passes and shows the red
   loss flag on 60/40; the letter says so and invents no fit.
2. **A number by hand.** Type into the letter a loss the app never printed, such as −18%.
   *Expect:* the app flags it.
3. **A fresh chat with no skill:** "My client can lose at most 25% in a year and has $100,000.
   What should they hold, and how much could they lose in a bad year?" Compare with your letter:
   where did its numbers come from?
