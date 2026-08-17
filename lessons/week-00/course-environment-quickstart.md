# Course Environment Quickstart — Get One Evidence-Producing Run

Use the smallest supported path that works. Week 1 verifies readiness live; this page helps you
arrive with either a successful run or an exact error the course can diagnose. Do not buy a tool
or paste credentials into a command, notebook, repository, or AI system.

## Path A — Local Python for labs

1. Install Python 3.11–3.14 from an approved source and confirm `python --version`.
2. Download `requirements-course.txt` from this Start Here module into your working folder.
3. In PowerShell on Windows, run:

```text
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-course.txt
```

On macOS/Linux, replace `.venv\Scripts\python` with `.venv/bin/python`.

4. Open the **Week 1 — Technology Readiness, DRIVER & Company Screening** card, download the
   **Preflight Check** file (`preflight_check.py`), and run it with the same environment Python.
5. Preserve the command, first error or success output, Python version, and operating system.

## Path B — Colab no-install route

Open a fresh Colab notebook, upload `requirements-course.txt`, and run this in the first cell:

```text
!python -m pip install -r requirements-course.txt
```

Upload and run the Week 1 preflight in that notebook. Colab is a supported lab route; the major
projects still require a locally runnable repository/application or an approved equivalent path.

## Project-only addition

Do not install the project stack for ordinary labs. When a project requires Streamlit, use the
separate `requirements-project.txt` instructions and freeze the versions actually tested in the
submitted repository.

## If the run fails

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
