<!-- AUTHORED HOME. Built under the 2026-09-06 rulings in OWNER-DECISION-GATES.md (Desktop VS Code;
     instruction, not materials; no offline route; one thing per lab; not our business; voice). -->

# Lab 05 — Build and Validate an FCFF DCF

**One thing today: build the model from the instruction, and prove it on the known answer.**

**Category:** Tuesday completion checkout, **25 or 0**.

**You arrive with:** your Course/Work Folder · the worked example · VS Code and Python installed
· your Lab 04 AI chat.

## Open your workspace

1. **VS Code → File → Open Folder** → your Course/Work Folder → **Open**. Trust the authors: **Yes**.
2. **Terminal → New Terminal.**
3. Type `python --version`. *Expect:* `Python 3.1x`. Windows: try `py --version`. macOS:
   `python3 --version`. The one that answers is your command all semester.

No folder yet? See previous lab instructions. Nothing from the course goes on your machine: read
the course on GitHub, build in your folder.

**AI partner:** the **Google Antigravity** extension (Extensions → search *Google Antigravity* →
Install → sign in with a Google account; the free plan is enough), or any AI in a browser tab.
Nothing graded needs an extension or an account.

**Something not working?** Debug with your AI: paste the exact command and the exact error text.

## D — the question, the same for everyone

> **What is one share of your company worth on a five-year FCFF DCF — and what growth does
today's price already assume?**

Paste it into your Lab 04 chat. Today you build the tool; Thursday you feed it your company.

## R — the five inputs (read them; source nothing today)

| Input | Training value | What it is |
|---|---|---|
| Starting FCFF | 100 USD millions | last year's free cash flow to the firm |
| Growth, Years 1–5 | 8%, 6%, 5%, 4%, 3% | a stated fade |
| WACC | 10% | the discount rate — never copy it onto your company |
| Terminal growth | 3% | growth after Year 5; must stay below WACC |
| Cash · debt · diluted shares | 50 · 300 · 50 | the bridge from the business to one share |

Thursday the same five rows come from your company's filing.

## I — build the model from the instruction

1. Right-click your folder → **New File** → `dcf.py`.
2. Send this to your AI partner:

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

3. Copy only the code it returns, paste it into `dcf.py`, save.
4. Run `python dcf.py`. *Expect:* twelve labelled lines; debug until no error.

## V — prove it on the known answer

| Output | Known answer |
|---|---:|
| FCFF Year 1 | 108.0000 |
| FCFF Year 2 | 114.4800 |
| FCFF Year 3 | 120.2040 |
| FCFF Year 4 | 125.0122 |
| FCFF Year 5 | 128.7625 |
| Present value of the explicit FCFF | 448.4408 |
| Terminal value at Year 5 | 1,894.6486 |
| Present value of the terminal value | 1,176.4277 |
| Enterprise value | 1,624.8685 |
| Equity value | 1,374.8685 |
| Value per diluted share | 27.4974 |
| Present value of the terminal value as a share of enterprise value | 0.7240 — that is 72.40% |

All twelve within a cent, or the model is wrong: debug with your AI until they match. The classic
error is a terminal value discounted six years instead of five.

**Prove it computes.** Set WACC to `0.11`, save, rerun. *Expect:* value per share about
**23.41**. Set it back to `0.10`. Write down what you saw — that is Thursday's first prediction.

## Evolve — skip in class, do it on your own

## Reflect

Explain to your partner:

1. the coding logic;
2. how WACC moves the value.

## Reversed DCF

**Learn on your own**

1. What is Reversed DCF;
2. How does it work;
3. Explain it.

## Checkout — on GitHub

**GitHub links of your files: md, py and/or other files as needed.**

**Thursday preview:** your company goes through this model in reality — DCF valuation, Reversed
DCF, and a grid that shows how fragile the number is.
