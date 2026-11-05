# Week 11 — AI Skills: Investors as Skills

## Mission

More AI, less finance: turn an investor's page from FAskills into a skill your AI runs the same way
every time — code computes every number from the 10-K, the model only judges.

Tuesday: Buffett as a skill, with a script on keyless SEC EDGAR data and a Streamlit app. Thursday:
Cathie Wood and Burry join him, a panel on one company, and a decision on whether to trust it.

## You arrive with

- Antigravity or Codex in VS Code; the Streamlit apps you built on live data (Lab 17);
- your partner.

## Outcomes

- Write a skill: a name and a description that tell your AI when to use it, and a bundled script.
- Download a company's 10-K facts from SEC EDGAR with no key, and print each number with its XBRL tag.
- Keep the numbers in code and the judgment in the model: a memo that uses only printed numbers, and
  an app that flags any number the script did not print.
- Keep honest gaps: "not found" and "not known", never an estimate.
- Run three investor skills on the same facts, read where they agree and split, and decide whether
  to trust the panel.

## Prerequisites and prework

**Before Tuesday — about 20 minutes.** Read your AI's skills page:
[Antigravity](https://antigravity.google/docs/skills) or
[Codex](https://developers.openai.com/codex/skills). Then read the
[FAskills README](https://github.com/CinderZhang/FAskills/blob/main/README.md) and
[Buffett's page](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md).
Ask: **what on Buffett's page could code compute, and what only judgment can?**

**Before Thursday — about 10 minutes.** On the holdings page of one of your Project 2 funds, find
its largest company and note its ticker. Read
[Cathie Wood's page](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/cathie_wood.md)
and [Burry's page](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/michael_burry.md).

## The two sessions

| Session | Lab | One thing |
|---|---|---|
| Tuesday | [Lab 18](lab-18-legend-investor-as-skill.md) | Buffett's page as a skill: code computes every number from the 10-K; the model only judges |
| Thursday | [Lab 19](lab-19-legend-panel.md) | Cathie Wood and Burry join him: a panel on one company, side by side in your app; trust it or not |

## Teams this week

Two people, the same partner; each keeps their own Project 2. Explain before you build, explain the
code both ways, argue bull and bear on Thursday. Checkouts stay individual.

## DRIVER this week

Define: the same question for everyone — can an investor's philosophy become a skill your AI runs
the same way every time? Represent: the investor's page and the rules your numbers follow.
Implement: the skill, its script and the app, from your own request. Validate: Costco's known
answer, JPMorgan's gaps and a hand-typed number the app must flag. Evolve: the panel on your fund's
largest company. Reflect: what the skill makes the same every time, and what it leaves to the model.

## Package map

- [Lab 18](lab-18-legend-investor-as-skill.md) and [Lab 19](lab-19-legend-panel.md) — the labs.
- [Student handout](student-handout.md) — the rules, the EDGAR endpoints, the digits once.
- [Open challenge](open-ended-challenge.md) — after class.
- [Prework](student-prework.md) — generated from the prework section above.
- Instructor guide, grading key and verification record — instructor only, not published.

## Brightspace order

Overview → Lab 18 → Lab 19. The Brightspace module carries the standard pointer to this page.
