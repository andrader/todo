## 1. Overview

You will build a small TODO / Checklist application intended for personal use on a local machine.
The purpose of this take-home exercise is to evaluate:

Your ability to work end-to-end on a small software project
Your reasoning, documentation quality, and scoping decisions
Your understanding of basic software engineering practices
(tests, CI, persistence, clarity, and structure)


## 2. Functional Requirements

Your TODO app must include at least the following:

### 2.1. Required Features

Create tasks
Required: title
Optional: description
Mark tasks as completed / uncompleted
List tasks
Show active tasks
Show completed tasks
Persistent storage
Tasks must remain available after the application restarts
You may use JSON, SQLite, or any lightweight local storage
Edit and delete tasks

### 2.2. Optional Features (Nice-to-Have)

Not required, but allowed if you have time:

Due dates / reminders
Priority or tags
Filters or search
Categories or grouping
Natural-language input (“Pay rent tomorrow at 9am”)
Keyboard shortcuts
If you mention or partially build any of these features, you must document whether they were intentionally left incomplete.


## 3. Allowed Technologies


Python full-stack using Streamlit

## 4. Deliverables


Submit a GitHub repository link

Your submission must include a `metadata.txt` file with the following information:

This file must contain:

Time spent
A number aligned with the client expectation (~60 minutes of coding)
AI tools used
List the tools (e.g., ChatGPT, Claude, GitHub Copilot) and how you used them
Features implemented
Features not implemented (and why)
Time constraints
Out of scope
Not required
Potential future improvements
Being explicit here is essential to avoid negative reviewer feedback.



## 5. Codebase
Your project must include:

Application source code
Tests (basic unit tests minimally required)
A complete README.md with:
Setup instructions
Install/prerequisites
How to run the app
How to run tests
Implemented features
Known limitations
GitHub Actions workflow (.github/workflows/CI.yml)
Must run on Ubuntu
Must install dependencies
Must run linting
Must run tests
Must pass successfully

6. README Requirements
Your README.md must contain:

6.1. Project Overview
Describe the structure, framework, and major components.

6.2. How to Install and Run
Include clear commands such as:

uv run streamlit run app.py

uvicorn app.main:app --reload

6.3. How to Run Tests
Include precise commands such as:

pytest

6.4. Scope & Known Limitations (Mandatory)
You must explicitly list:

Implemented:
CRUD operations
Persistence
Completion toggle
Tests
Not Implemented:
Any optional features you skipped
Any partially implemented features
This section prevents confusion during evaluation.


## 7. CI Requirements
Your GitHub Actions workflow must:

Use Ubuntu runner
Install dependencies
Run linters (e.g., flake8, ruff, black --check, or .NET format)
Run tests
Pass successfully



## 9. Common Mistakes to Avoid
❌ Submitting an incomplete project without documenting limitations
Always list what you intentionally left out.

❌ Declaring unrealistic or contradictory time spent
Your repository, commit timestamps, and logs must align with the declared ~60-minute expectation.

❌ A README that lacks setup instructions
The reviewer must be able to run your project easily.

❌ CI that fails
Ensure the workflow passes before submitting.


## 10. Evaluation Criteria

Your submission will be evaluated based on:

Amount of functionality
Code quality and architecture
Correctness and stability
Tests and linting
Documentation clarity
