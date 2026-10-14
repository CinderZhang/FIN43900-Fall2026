# Week 9 — Portfolio Construction and Optimization

## Mission

Tuesday: build a risk engine from an instruction and price three simple portfolios for the
Meridian Foundation, the training case from Lab 13. Thursday: turn your engine into your first app —
a Streamlit web page that finds the lowest-risk mix meeting the mandate — test whether its answer
survives a one-point change, then load your own Project 2 universe into it.

**GitHub is the main delivery.** Every lab and project is handed in as GitHub links to your own
files.

## You arrive with

- your Lab 13 `mandate.py`, your Lab 13 chat, and your Course/Work Folder;
- your own Project 2 mandate, written after Lab 13 in its shape.

## Outcomes

- Build a covariance matrix from volatilities and correlations, and say why correlation lowers risk.
- Price three baselines and read them against a client's mandate.
- Turn your Python engine into a Streamlit web app and prove it against a known answer.
- Find the lowest-risk mix that meets an objective under a constraint, by a search you can check.
- Show how far that mix moves when one estimate moves, and make an adopt, pilot or reject call.

## Prerequisites and prework

**Before Tuesday — about 30 minutes.**

1. Read [OpenStax Principles of Finance §15.2](https://openstax.org/books/principles-finance/pages/15-2-risk-and-return-to-multiple-assets)
   from **"Diversification"** through **"Portfolio Size and Risk"** (8–10 minutes). Ask: **why can
   two risky assets together be less risky than either alone?** The
   [handout's diversification section](student-handout.md#diversification-in-plain-language) is
   the complete alternative.
2. Work the benchmark's volatility by hand from the [handout's digits](student-handout.md#the-digits-once).
   You will explain it to your partner first thing.

**Before Thursday — about 35 minutes.**

1. From your own mandate, choose three to six funds for your universe (cash, bonds, fixed income,
   equity — the [end of Lab 14](lab-14-portfolio-baselines.md#before-thursday--your-own-universe-in-funds)
   shows how), and write down your objective as a number and your one hard constraint.
2. Build your `prices.csv` for those funds, as the end of Lab 14 says: five years of monthly
   **Adj Close** prices, each ticker's source and download date in your `.md` file.
3. Install Streamlit, the Python library that turns a script into a web page, and run its demo:
   [Streamlit's install page](https://docs.streamlit.io/get-started/installation/command-line). Then read
   [Basic concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts) through **Data flow**.
   Ask: **what happens to my script each time someone moves a control?**

## The two sessions

| Session | Lab | One thing |
|---|---|---|
| Tuesday | [Lab 14](lab-14-portfolio-baselines.md) | the risk engine, proved on Meridian |
| Thursday | [Lab 15](lab-15-portfolio-stability.md) | your first app: the lowest-risk mix and its stress test, on Meridian and on your universe |

## Teams this week

Two people; keep the partner you had in Week 8. Each of you keeps your own Project 2; a team therefore holds two
universes. Your partner's job is named in each lab: explain before you build, swap and break on
Tuesday, attack one estimate on Thursday. Checkouts stay individual.

## DRIVER this week

Define: the same question for everyone — what does each portfolio earn and risk, and does the
lowest-risk mix survive a small change? Represent: the inputs, labelled as training values or your
estimates. Implement: the engine from one request. Validate: the known answer, the correlation
probe, the partner's break. Evolve: the search and the stress run as a Streamlit app, Meridian first, then yours.
Reflect: to your partner, why the answer moved.

## Package map

- [Lab 14](lab-14-portfolio-baselines.md) and [Lab 15](lab-15-portfolio-stability.md) — the labs.
- [Student handout](student-handout.md) — diversification, the digits once, the rules.
- [Open challenge](open-ended-challenge.md) — after class.
- [Prework](student-prework.md) — generated from the prework section above.
- Instructor guide, grading key and verification record — instructor only, not published.

## Brightspace order

Overview → Lab 14 → Lab 15. The Brightspace module carries the standard pointer to this page.
