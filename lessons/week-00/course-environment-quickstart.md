# Course Environment Quickstart — Optional Head Start and Recovery Reference

**Nothing on this page is required before class.** All technical setup — Colab, ChatGPT,
Gemini, the readiness check — happens **together, step by step, in Tuesday's Week 1 class**,
with the instructor projecting every click and TAs walking the rows. Nothing technical is
graded before that guided setup. Use this page only if you *want* a head start, or later in
the term as the recovery reference when an environment breaks. Do not buy a tool or paste
credentials into a command, notebook, repository, or AI system.

## Path A — Colab, the course path (no install)

1. Open [colab.research.google.com](https://colab.research.google.com) and sign in with
   Google. Click **New notebook**.
2. Download `requirements-course.txt` from this Start Here module.
3. In the notebook, click the **folder icon** (left sidebar) → **upload** icon → select
   `requirements-course.txt`. Then paste this into the first cell and press **Run** (▶):

```text
!python -m pip install -r requirements-course.txt
```

4. Optionally, upload and run the Week 1 **Preflight Check** file (`preflight_check.py`) from
   the **Week 1 — Technology Readiness, DRIVER & Company Screening** card the same way. A green
   diagnostic block means READY.
5. If anything fails, preserve the exact first error message — that is useful evidence, not a
   problem. Tuesday's class diagnoses it with you.

Colab is a supported lab route all semester; the major projects still require a locally
runnable repository/application or an approved equivalent path, taught when the projects need it.

## Path B — Local Python (optional, later; never required for labs)

Skip this before Week 1 unless you already work in a local Python setup and want one. Install
Python 3.11–3.14 from an approved source, confirm `python --version`, then in PowerShell on
Windows run:

```text
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-course.txt
```

On macOS/Linux, replace `.venv\Scripts\python` with `.venv/bin/python`. Run the Week 1
preflight with the same environment Python. Preserve the command, first error or success
output, Python version, and operating system.

## Project-only addition

Do not install the project stack for ordinary labs. When a project requires Streamlit, use the
separate `requirements-project.txt` instructions and freeze the versions actually tested in the
submitted repository.

## If a run fails

Stop after one documented attempt. Use the Starter Help Ladder only at the level permitted by the
current task's AI Boundary Card. Bring the Python version, command, complete first error, and one
attempted fix to Week 1 or the Support Map route. The offline lab fallback preserves honest
progress while the environment is repaired.

## Optional QuantEcon recovery map — one blocker, one page

This is not required prework. Stop after the smallest named page/section that resolves the first
blocker, then rerun the course preflight. Do not read the whole book.

| Diagnosed blocker | Exact QuantEcon page/section | Recovery budget |
|---|---|---:|
| launching Python/Jupyter or running a first cell | [Getting Started](https://python-programming.quantecon.org/getting_started.html), through the first successful execution only | 10–15 min |
| variables, conditionals, loops, collections, or basic syntax | [Python Essentials](https://python-programming.quantecon.org/python_essentials.html), only the matching heading | 10–20 min |
| array shape, indexing, vector operations, or numerical types | [NumPy](https://python-programming.quantecon.org/numpy.html), only the matching heading | 10–20 min |
| loading, selecting, or inspecting tabular data | [Pandas](https://python-programming.quantecon.org/pandas.html), through the first matching DataFrame example | 10–20 min |
| reading a traceback or isolating the first failing line | [Debugging and Handling Errors](https://python-programming.quantecon.org/debugging.html), only the traceback/debugging section | 10–15 min |
| notebook/browser/package symptom not explained above | [Troubleshooting](https://python-programming.quantecon.org/troubleshooting.html), only the named symptom | 5–10 min |

Bring the exact command, complete first error, page used, and what changed. QuantEcon examples are
recovery references; the FIN 43900 requirements file and preflight remain the controlling setup.
