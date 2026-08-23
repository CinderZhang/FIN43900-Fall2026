# FIN 43900 — Major Project Submission Architecture

> **Status:** instructor decision recorded 2026-08-14. This architecture applies uniformly
> to Project 1, Project 2, and the Capstone. It changes the required evidence package, not
> the published project points or deadlines in the syllabus schedule and assignment pages.

The student-facing **AI Boundary Card — Use This All Semester** is the stable interpretation of permitted tools,
the exact receipt boundary, ambiguous integrated AI, accidental early use, and post-checkpoint
evidence. Project briefs may narrow it but may not silently contradict it.

## Purpose

Each major project must show three different kinds of professional ownership:

1. **Research evolution:** what the student concluded before AI assistance, whether and how
   the conclusion changed, and what evidence justified the changed or unchanged position.
2. **Technical ownership:** how the codebase works, how the output was produced, and how
   the student tested it.
3. **Investment judgment:** a concise recommendation defended as if the student were
   presenting to a buy-side investment committee.

The videos are evidence surfaces, not substitutes for the underlying work. The written
artifacts and repository must stand on their own when opened cold by a grader.

## Uniform submission bundle

Every project is individual. Every student submits their own version of the same **seven
conceptual parts** below; no team artifact can substitute for individual evidence. The upload
manifest expands those parts into **12 rows** so each video and transcript is independently
addressable: 11 required rows plus one optional deployed-output row. “Seven parts” and “12
manifest rows” describe different levels of the same package and are never interchangeable.

### 1. Timestamped Edition A checkpoint — before permitted project-specific AI

Edition A is declared by the student as authored without project-specific generative-AI assistance
and submitted as a PDF
through the designated Brightspace checkpoint before AI-assisted research or coding begins
for that project. Reading course materials, filings, academic or professional sources, and
using ordinary search, spreadsheet, calculator, and database tools are allowed and identified.
Using a generative model, AI search/summary tool, coding assistant, or AI-authored text or code
is not allowed until Edition A is submitted. Ambiguous tools are disclosed before use and
handled under one published instructor ruling applied to the whole class. Edition A records:

- the finance decision and intended user;
- the initial thesis, recommendation, or hypothesis;
- the evidence already known and its sources;
- the most consequential assumptions;
- what remains unknown or uncertain; and
- the research and validation plan.

The student attests that Edition A was prepared without generative-AI assistance. Project 1's
supervised Lab 03 may be described as observed pre-AI evidence. The unsupervised Project 2 and
Capstone windows establish declared baselines, not proof that AI was absent. The first successful
on-time Brightspace submission is the baseline of record: its timestamp fixes the
submission order and makes the comparison auditable, but does not by itself prove authorship.
Individual ownership is verified through later supervised changed-input/evidence-navigation work,
not by treating the attestation as forensic proof. Students do not overwrite Edition A after AI
use; a factual correction is filed as a dated
addendum immediately after the unchanged Edition A inside `Research-Evolution.pdf` and
`docs/research-evolution.pdf`. It supplements rather than modifies the baseline. Approved
accommodations, Special Access, and late-add cases receive a documented window before that
student's AI-assisted project work begins. A missing on-time Edition A cannot be recreated in
the final package; the A-to-B requirement is treated as absent evidence under Problem
Definition and Decision Usefulness, without a second penalty elsewhere. Edition B and Video 1
remain required: the student documents the current position, one consequential supporting
check, and one tested AI output, but receives no additional deduction merely because the
before/after comparison is unavailable.

### 2. Edition B research-evolution brief — after project-specific research and AI assistance

Edition B updates the analysis after documented AI-assisted research and development. It
must include a compact A-to-B change table:

| Changed item | Edition A | Edition B | Primary driver of change | Evidence or test that justified the change |
|---|---|---|---|---|
| Thesis/recommendation |  |  | course instruction / own analysis / peer challenge / AI / mixed |  |
| Data/source choice |  |  |  |  |
| Assumption or model design |  |  |  |  |
| Risk, limitation, or uncertainty |  |  |  |  |

Edition B ends with: **What changed from Edition A to Edition B, and why?** This is graded
as observable research and decision evidence, not as personality, confidence, effort, or
claimed personal growth. A supported conclusion that Edition A remains correct can earn full
credit: enter **No material change** and cite the evidence or test that confirmed it. The
graded object is the justification attached to each changed or unchanged position, not change
for its own sake.

Every final project also contains one **Locked Changed-Input Record** in
`Validation-and-AI-Use.pdf`: before any AI assistance on that prediction and before execution,
the student writes a human-authored prediction and records the exact material input and
old/new values, expected output direction, expected decision effect, timestamp, and repository
commit. The run itself is AI closed. After execution, the student preserves before/after output,
actual decision effect, reconciliation to the prediction, and a failure diagnosis or explanation
when the action does not change. This is required evidence—not a new rubric criterion or video.
Field completeness is necessary but not sufficient: credit depends on a finance-grounded prediction,
a faithful run, and a diagnosis supported by the preserved evidence.

### 3. GitHub repository and reproducible output

The repository may be public or private, but it must be accessible to the instructional
team. It contains:

- runnable source code and a dependency/environment file;
- a README stating the finance decision, intended user, setup and run instructions,
  repository map, data sources, and known limitations;
- traceable development history used only as corroborating evidence of ownership; commit
  volume, timing, or frequency is not graded separately;
- visible executed output or a clearly identified output artifact;
- `docs/research-evolution.pdf` containing Editions A and B;
- `docs/decision-memo.pdf` or `docs/decision-deck.pdf`;
- `docs/validation-and-ai-use.md` containing the working validation record and named AI-tool
  disclosure; its content must match the frozen Brightspace PDF at submission;
- `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt`, and
  `docs/transcript-video-3.txt`, matching the corrected submitted transcripts; and
- a `.env.example` with named but empty variables when credentials are needed, with no
  passwords, API keys, tokens, credentials, or private data committed anywhere.

A live deployment may be linked but is not required unless the specific Brightspace
assignment says otherwise. A locally runnable project and visible executed output are
required. “Visible executed output” means a grader can see the material inputs, as-of date,
and finance result in an included report, screenshot, notebook output, or application capture
without executing the code. The README and Video 2 must show how a clean user would reproduce
that result. References to AI use in other artifacts point to the complete record rather than
duplicating it. `Validation-and-AI-Use.pdf` in Brightspace is the authoritative frozen record
for grading and appeal; the repository Markdown file is its content-equivalent working source
as of the submission timestamp.

### 4. Video 1 — Research evolution and AI-output check

**Maximum duration: 3:00. Graders stop at 3:00.** Refer to Edition A and Edition B, identify
whether the consequential change was driven by course instruction, own analysis, peer challenge,
AI, or a mixture, then explain why the cited evidence was sufficient. Show at least one
AI-generated claim, suggestion, or result and the check
performed on it; state whether it was accepted, qualified, corrected, or rejected and why.
This video's unique function is to demonstrate authorship of the research decisions and the
checks performed on AI output, not to read the change table or deliver a generic reflection.

### 5. Video 2 — Detailed codebase walkthrough

**Maximum duration: 5:00. Graders stop at 5:00.** Open the submitted repository and explain
the architecture, data flow, key files or functions, financial logic, and how to reproduce the
output. Demonstrate the validation or changed-input test aimed at the project's highest-risk
financial or technical claim, and identify one failure mode, limitation, or unresolved risk.
This video's unique function is to demonstrate technical ownership; reading the README or
showing only the user interface is insufficient.

### 6. Investment-committee memo or decision deck

Submit a concise memo or deck that can be read without watching a video. It contains:

- the decision and recommendation first;
- the valuation, allocation, or decision range rather than false point precision;
- the strongest supporting evidence and the as-of date;
- material assumptions and sensitivities;
- principal risks, failure conditions, and monitoring triggers;
- the action requested from the committee; and
- a reference to the named AI-tool disclosure and material checks in the single AI-use record.

This artifact is the authoritative written statement of the recommendation and supporting
finance analysis. The specific project's intended user remains visible even when the student
presents the decision through an investment-committee simulation.

### 7. Video 3 — Buy-side investment-committee presentation

**Maximum duration: 5:00. Graders stop at 5:00.** A project brief may require a specific
opening segment inside this window — Project 1 requires a live product demonstration as
the video's main delivery — and that requirement is stated in the project's own brief.
Present as the assigned analyst to a
buy-side investment committee. Lead with the decision, not the build process. Defend the
recommendation, range, evidence, material assumptions, risks, and explicit conditions or
triggers. End with a clear committee ask. This video's unique function is to demonstrate the
student's ownership and defense of the final judgment; it does not repeat the detailed memo or
the code walkthrough. AI may assist preparation when disclosed, but the student owns every
claim, recommendation, and response presented.

All three videos use separate, descriptively titled YouTube links — **Unlisted or Public, the
student's choice; never Private** — or an approved Purdue-hosted equivalent. Public visibility
is a personal portfolio decision and is never graded in either direction. Links must remain
viewable by the instructional team through the grade-appeal window. Captions/transcripts are required; students review and correct finance
terms, tickers, names, and material numerical errors before submission. Each corrected
transcript is also submitted as a plain-text file so the grading and appeal record cannot
change with the hosting platform. Platform-generated captions or an automated transcript may
be the starting point; students correct substantive finance terms, names, tickers, speaker
attribution, and material numbers rather than polishing every harmless filler word. Consistent
with the syllabus, the recording includes a small
webcam view unless an approved accommodation uses an equivalent identity and ownership check.
Appearance, accent, confidence, and production polish are not graded; clear audio plus the
required visual evidence is enough. Approved accommodations may use an equivalent recorded or
scheduled format that preserves the same evidence; an extended duration applies when required
by the approved accommodation. The assignment page publishes the uniform alternative process.

The final Brightspace submission contains:

- a manifest with the repository URL, three video URLs, optional deployed-output URL, a
  timestamped evidence index for each video's required elements, and the private-repository
  access confirmation;
- `Research-Evolution.pdf` containing the unchanged Edition A and final Edition B;
- `Decision-Memo.pdf` or `Decision-Deck.pdf`; and
- `Validation-and-AI-Use.pdf`, matching the repository's working source; and
- three corrected plain-text transcript files, one for each video.

These Brightspace attachments are the frozen grading and appeal record. Content-equivalent
copies as of the submission timestamp also remain in the repository so the project is
self-contained. The manifest records each video's provider, stable video ID or URL, title, and
duration; the submitted recording may not be replaced or edited after the deadline. The
instructional-team GitHub access identity and filename prefix for each project are published on
the assignment page before the Edition A checkpoint opens.

### Capstone-only extensions

The capstone brief extends this shared architecture without changing it for Projects 1–2:

- **Durations:** capstone videos run longer — Video 1 max 6:00, Video 2 max 10:00, Video 3
  max 8:00. Projects 1–2 keep the durations above.
- **Two additional manifest rows** (14 total): the **launch-post draft** (a Substack-ready
  written product story; the draft is required, publishing it is optional and never graded)
  and the **AI-component pointer** (the file/function where the required generative-AI
  component lives, with its validation evidence location).
- The capstone brief defines the required AI component and its access route; its validation
  evidence lives in the standing `Validation-and-AI-Use.pdf` record, not a new surface.

## Project-specific professional role

The evidence architecture stays identical; only the finance decision changes.

| Project | Student role | Investment-committee decision |
|---|---|---|
| Project 1 — Corporate Finance Application | Equity research analyst advising a committee with no current position | Initiate, watch/defer, or do not initiate the target company, supported by a defensible valuation range and conditions |
| Project 2 — Investment Management Application | Portfolio or quantitative analyst | Adopt, allocate to, rebalance, pilot, or reject the proposed strategy under explicit objectives and constraints |
| Capstone — Integrated Financial Analysis System | Lead analyst | Recommend approval, revision, deferral, or rejection of the integrated system, with cross-component risks and monitoring triggers |

## Relationship to the existing rubric

The six project criteria and weights remain unchanged. The authoritative performance levels,
descriptors, 300/400-point mappings, calibration procedure, and scoring examples are in
`MAJOR-PROJECT-ANALYTIC-RUBRIC.md`. The bundle provides multiple observable evidence surfaces
for those criteria:

| Existing criterion | Primary evidence |
|---|---|
| Problem definition and decision usefulness | Edition A, Edition B, decision memo/deck, Videos 1 and 3 |
| Data integrity and traceability | repository, README, Edition B, validation record |
| Financial soundness and judgment | decision memo/deck and Video 3 defense |
| Technical execution and usability | repository, executed output, Video 2 |
| Validation, sensitivity, and reproducibility | validation record, Video 1 AI-output check, Locked Changed-Input Record, Video 2 |
| Professional communication | all written artifacts and Videos 1–3 |

No video earns points merely for existing. Graders assess the evidence under the published
criteria and do not deduct twice for one defect. Professional communication means structure,
accuracy, precision, audience fit, and a coherent evidence trail; it does not mean accent,
personality, confidence, camera presence, or production polish.

The written Brightspace artifacts govern the substantive recommendation, data, assumptions,
and reported results. The videos govern evidence of authorship, technical ownership, and oral
defense. An unexplained conflict is scored once under the relevant substantive criterion and
may also affect Professional Communication only when the conflict itself makes the package
unclear. Criterion scores are recorded normally; then the syllabus-level 50% total-score cap
is applied when visible executed output is absent. The cap is not a second line-item deduction.
A repository of code alone is not executed output.

Before Project 1 grading, the assignment page publishes observable performance anchors for
each criterion, including the treatment of missing Edition A, weak ownership evidence,
inaccessible links, contradictions, and absent executed output. The learner object **Project 1 —
Annotated Decision-Evidence Excerpt and Non-Example** supplies the promised annotated excerpt and
non-example. The instructor and TAs norm-set on the same sample
before releasing grades. No assignment-local copy may silently change a criterion, weight,
level factor, cap, or no-double-deduction rule from `MAJOR-PROJECT-ANALYTIC-RUBRIC.md`.

## Standard grading workflow

The three videos total no more than 13 minutes, but grading does not require three blind linear
viewings for every student. The standard sequence is:

1. verify the Brightspace receipt, required attachments, links, repository access, and caption
   availability;
2. read the research-evolution artifact and decision memo/deck;
3. inspect the README, visible executed output, validation record, and only the code needed to
   confirm a material claim;
4. use the manifest's timestamp index and corrected transcript to review the required moments
   in Videos 1–3; expand to full playback when the transcript is missing or materially garbled,
   a required visual demonstration cannot be verified at the indexed time, written and video
   evidence conflict, or a documented ownership/integrity flag requires verification; record
   the timestamps reviewed and the escalation reason; and
5. score one six-criterion rubric and record any access or integrity flag separately.

This workflow makes the three distinct ownership surfaces reviewable at approximately 110-
student scale while preserving the instructor's ability to inspect any full artifact. The
instructor fully reviews a fixed 10% sample of otherwise transcript-first submissions in each
project to audit consistency across graders and sections.

## Brightspace build requirements

For each major project, build:

1. one Edition A checkpoint with a published availability window and a timestamped receipt;
2. one final assignment with a required link/file manifest and the six-criterion rubric;
3. one student-facing checklist using the seven bundle headings above;
4. one submission template with consistent filenames and link labels; and
5. one Demo Student test covering missing files, filename/link labels, private-repository
   access for all graders in both sections, all three videos and corrected transcripts,
   attachments, resubmission and baseline-of-record behavior, Special Access, broken or
   deleted links, grade association, and receipt visibility.

The Edition A checkpoint is always a **separate ungraded Brightspace assignment object**. A lab
checkout may require its receipt/attempt identifier as evidence, but a graded or droppable lab
never stores, substitutes for, or determines whether the Edition A baseline exists.

The final assignment states that an inaccessible required link at grading time is missing
evidence. Before release, choose and publish one uniform short cure process for access-setting
mistakes; it may restore access but may not replace or revise the underlying work.
