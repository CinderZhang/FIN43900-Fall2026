# Week 8 Student Handout — The Mandate Comes First

Last month: what is one company worth? Project 2: what should a portfolio hold, for whom, under
which rules? Before anyone builds a portfolio, the client's words become rules.

**GitHub is the main delivery from now on.** Every lab and project is handed in as GitHub links to
your own files. This week: [Lab 13](lab-13-portfolio-mandate.md), on your own after the guest talk.

## The command

In the VS Code terminal (**Terminal → New Terminal**), with your own Python command (`python`,
`py`, or `python3` — the one that answered in Week 3):

| Command | Expect |
|---|---|
| `python mandate.py` | the reserve minimum, then each candidate's rules with pass or FAIL and a verdict |

Something breaks? Debug with your AI: the exact command and the exact error text.

## The rules

- Sort before you build, without AI. Every client statement is an objective, a hard constraint, a preference,
  an unverifiable promise, or missing.
- A rule the client did not define is not tested. The checker prints "requires CIO clarification";
  nobody invents the number.
- Compute every threshold from the facts. The reserve minimum is quarters × payout ÷ reserve size.
- Passing every checkable rule is not the same as suitable. Name the statement that decides.
- One question back to the client beats a guess.

## After the lab

Lab 13 uses the **assigned common case**. Then write your own Project 2 mandate in the same shape:
objective, hard constraints, the one question for your client. Project 2 starts from it in Week 9.

## DRIVER, one line each

Define — the same question for everyone. Represent — the CIO's statements, sorted. Implement — the
checker from one request. Validate — the known answer and the probe. Evolve and Reflect — your AI
attacks the checker; you judge it.
