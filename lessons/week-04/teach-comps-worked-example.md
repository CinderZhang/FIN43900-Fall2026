# The Training-Case Comps, Worked End to End

*This page teaches. Rules and submission requirements live in the Week 4 handout and Labs
07–08. The figures below are the official Week 4 training case — the same numbers your Lab 07
work must reproduce. This is a different synthetic company from Week 3's DCF case; do not mix
their numbers.*

## Why a committee wants a second opinion

Your DCF is an argument about the future. Multiples are a report about the present: what real
buyers are paying, right now, for businesses like yours. Neither settles the question alone —
a DCF can be internally perfect and built on a fantasy, and multiples can dutifully copy the
market's current mood. The craft is using each to interrogate the other. That starts with the
most abused word in finance: *comparable*.

## The case

Your target earned **EBITDA of $80M** and **net income of $40M**. It holds **$50M cash**,
owes **$300M debt**, and has **50M diluted shares**. Your policy passed four peers:

| Peer | EV ($M) | EBITDA ($M) | Equity value ($M) | Net income ($M) |
|---|---:|---:|---:|---:|
| Alpha | 1,200 | 120 | 900 | 75 |
| Beta | 1,600 | 100 | 1,200 | 60 |
| Gamma | 900 | 100 | 750 | 50 |
| Delta | 2,000 | 125 | 1,500 | 100 |

A qualified precedent transaction closed at **14× EV/EBITDA**.

## Step 1 — Compute each peer's multiples yourself

Never accept a multiple you didn't compute — providers disagree on definitions, and Week 1
showed you how badly. One by hand:

> Alpha EV/EBITDA = 1,200 / 120 = **10.0×**

| Peer | EV/EBITDA | P/E |
|---|---:|---:|
| Alpha | 10.0× | 900 / 75 = 12.0× |
| Beta | 16.0× | 1,200 / 60 = 20.0× |
| Gamma | 9.0× | 750 / 50 = 15.0× |
| Delta | 16.0× | 1,500 / 100 = 15.0× |

**Read the dispersion before any average.** EV/EBITDA runs from 9× to 16× — nearly a factor
of two, for companies your own policy called comparable. That spread *is* information: either the market
prices real differences your policy ignored (growth, margins, risk), or some peer doesn't
belong. Investigate Beta and Delta versus Gamma before proceeding; "comparable" was doing
heavy lifting.

## Step 2 — Take the median, and know why

> Median EV/EBITDA = median(10.0, 16.0, 9.0, 16.0) = (10.0 + 16.0) / 2 = **13.0×**
> Median P/E = median(12.0, 20.0, 15.0, 15.0) = **15.0×**

Median, not mean, because with four peers a single outlier drags a mean wherever it likes.
And notice what you just did: you replaced four market opinions with one number. The range
(9–16×) rides along with your answer from here on — that is why Lab 07 asks for an implied
*range*, not a point.

## Step 3 — Apply the enterprise multiple (the bridge returns)

EV/EBITDA is an **enterprise** multiple: it prices the whole operating business. So applying
it gives you enterprise value, and you must cross the same bridge you built in Weeks 2–3:

> EV = 13.0 × 80 = 1,040
> Equity = 1,040 + 50 − 300 = 790
> Per share = 790 / 50 = **$15.80**

## Step 4 — Apply the equity multiple (no bridge — and that's the trap)

P/E is an **equity** multiple: net income already belongs to shareholders alone, after
interest. Applying it lands directly on equity value:

> Equity = 15.0 × 40 = 600 → 600 / 50 = **$12.00**

Bridging a P/E answer — adding cash, subtracting debt — double-counts the capital structure
and is one of the most common junior errors in existence. One sentence to keep: *enterprise
multiples need the bridge; equity multiples already crossed it.*

## Step 5 — The precedent transaction

> EV = 14.0 × 80 = 1,120 → 1,120 + 50 − 300 = 870 → **$17.40 per share**

The deal multiple (14×) sits above the trading median (13×). Before using it, ask what a
buyer of the *whole company* paid for that trading multiples don't include: control, expected
synergies, a competitive auction, a different point in time. If you cannot defend the deal's
context — Lab 08's whole subject — you qualify it or set it aside; you don't quietly average
it in.

## Step 6 — Three answers, one analyst

| Route | Per share |
|---|---:|
| Trading EV/EBITDA (13×) | $15.80 |
| Trading P/E (15×) | $12.00 |
| Precedent transaction (14×) | $17.40 |

The spread from $12.00 to $17.40 is not a failure — it is the finding. Each method prices a
different thing: P/E carries this target's leverage and below-the-line items; EV/EBITDA
prices operations; the precedent embeds control and its moment in time. Your job — and
Project 1's explicit requirement — is to *explain* the disagreement and say which evidence
best fits the committee's question. Mechanically averaging the three numbers destroys
exactly the information the spread contains.

## Choosing peers before you meet them — the policy discipline

The peer table above didn't fall from the sky; a policy admitted it. Write the policy before
you see any candidates (Lab 07 enforces this order), on dimensions like these:

| Dimension | Ask | Typical weight |
|---|---|---|
| Business model | same revenue model and economics? | high |
| Growth profile | similar expected growth? | high |
| Margins / capital intensity | comparable profitability structure? | medium |
| Scale | same order of magnitude? | medium |
| Geography / regulation | same markets and rules? | situational |

Then audit every candidate — AI-suggested ones especially: still public? still operating
(not acquired)? business model actually matches? current financials available? material
differences named? You are validating a list, never accepting one.

## Check yourself

1. Compute Beta's P/E from the table without looking at Step 1.
2. A teammate applies the 13× EV/EBITDA multiple and reports 1,040 / 50 = $20.80 per share.
   Name the error in one sentence.
3. Why might Gamma trade at 9× while Beta trades at 16× — give two legitimate reasons and
   one illegitimate one.
4. The precedent implies $17.40 and trading implies $15.80. A colleague says "average them:
   $16.60." What do you say?

*Answers: (1) 1,200 / 60 = 20.0×. (2) They skipped the bridge — 1,040 is enterprise value,
not equity; debt and cash must be netted first. (3) Legitimate: faster expected growth,
structurally higher margins/lower risk; illegitimate: "the data provider said so" — a
definition or period mismatch isn't a valuation reason. (4) The $1.60 gap is evidence about
control value and deal context; averaging erases the question the committee is paying you to
answer.*
