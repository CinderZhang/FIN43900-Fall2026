# Session 5 — Your DCF, in a Real Workspace

> **One thing today: build the model from the instruction, and prove it on the known answer.**

---

## Today's run of show

1. Workspace
2. **D** question
3. **R** inputs
4. **I** build; **quiz when told**
5. **V** known answer
6. **Reflect**; **Reversed DCF**
7. Checkout — GitHub

[Lab 05](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-05-dcf-build.md)

---

## Workspace alive

1. **VS Code → File → Open Folder** → your Course/Work Folder. Trust the authors: **Yes**.
2. **Terminal → New Terminal.**
3. `python --version`. **Expect:** `Python 3.1x`. Windows `py`, macOS `python3`.

**AI partner:** **Google Antigravity** extension (Extensions → search → Install → sign in), or
any AI in a tab.

---

## D — the question, the same for everyone

> **What is one share of your company worth on a five-year FCFF DCF — and what growth does
today's price already assume?**

Paste it into your Lab 04 chat.

---

## R — the five inputs

| Input | Training value | What it is |
|---|---|---|
| Starting FCFF | 100 USD millions | last year's FCFF |
| Growth, Years 1–5 | 8%, 6%, 5%, 4%, 3% | a stated fade |
| WACC | 10% | discount rate — never copy it |
| Terminal growth | 3% | after Year 5; below WACC |
| Cash · debt · shares | 50 · 300 · 50 | business to one share |

Source nothing today.

---

## I — build from the instruction

1. Right-click your folder → **New File** → `dcf.py`.
2. Send this, then read the next slide:

   > Write one Python file, `dcf.py`, using only Python's standard library — no packages to
   > install. At the top, a block of inputs I can edit by hand: starting FCFF in USD millions;
   > five yearly growth rates; WACC; terminal growth; non-operating cash; debt; diluted shares
   > in millions. Fill them with these training values: FCFF 100; growth 0.08, 0.06, 0.05,
   > 0.04, 0.03; WACC 0.10; terminal growth 0.03; cash 50; debt 300; shares 50. Convention:
   > annual end-of-year FCFF, five explicit years, a Gordon-growth terminal value at the end of
   > Year 5 discounted five years, then equity value = enterprise value + cash − debt, divided
   > by diluted shares. Stop with a clear message if terminal growth is greater than or equal
   > to WACC. Compute every number from the inputs — never type an answer in — and print
   > twelve labelled lines to four decimals: FCFF for Years 1 to 5; present value of the five
   > explicit FCFF; terminal value at Year 5; present value of the terminal value; enterprise
   > value; equity value; value per diluted share; and the present value of the terminal value as a share of enterprise
   > value. I have the known answers and will check every line. Then give me the exact command
   > to run it, and explain in two sentences why the terminal value is discounted five years
   > and not six.

3. Paste only the code into `dcf.py`, save.
4. `python dcf.py`. **Expect:** twelve labelled lines; debug until clean.

---

## V — prove it on the known answer

| Output | Known answer |
|---|---:|
| FCFF Year 1 | 108.0000 |
| FCFF Year 2 | 114.4800 |
| FCFF Year 3 | 120.2040 |
| FCFF Year 4 | 125.0122 |
| FCFF Year 5 | 128.7625 |
| PV of explicit FCFF | 448.4408 |
| Terminal value, Year 5 | 1,894.6486 |
| PV of terminal value | 1,176.4277 |
| Enterprise value | 1,624.8685 |
| Equity value | 1,374.8685 |
| Value per share | **27.4974** |
| PV of TV ÷ enterprise value | **0.7240** (72.40%) |

All twelve within a cent, or debug with your AI. Classic error: six-year terminal discount.

**Prove it:** WACC `0.11`, save, rerun. **Expect:** about **23.41**. Back to `0.10` —
Thursday's first prediction.

---

## Reflect · Reversed DCF

**Explain to your partner:** 1. the coding logic; 2. how WACC moves the value.

**Evolve:** skip in class.

**Learn on your own:**

1. What is Reversed DCF;
2. How does it work;
3. Explain it.

---

## Checkout — on GitHub

**Brightspace → Quizzes → Lab 05.**

**GitHub links of your files: md, py and/or other files as needed.**

**Thursday:** your company through this model in reality — DCF valuation, Reversed DCF, and a
grid that shows how fragile the number is.
