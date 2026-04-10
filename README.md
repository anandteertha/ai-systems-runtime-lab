# AI Systems Runtime Lab

This repository is a systems-focused learning lab for understanding how
programs execute, how memory is organized at runtime, and how those core
concepts connect to building efficient AI systems.

The repo currently contains one foundational project:

- `1. Program_Anatomy_Explorer`: a small C++ program plus study notes that
  explain what happens when code becomes a running process.

## Why this repo exists

Before optimizing AI inference, batching requests, or managing model memory,
it helps to understand the lower-level execution model underneath all of that.

This lab is meant to build intuition around:

- program vs process
- compilation and linking
- process memory layout
- stack vs heap behavior
- recursion and stack frames
- how variable lifetime maps to memory regions

## Current project

### 1. Program Anatomy Explorer

This project demonstrates how a simple C++ program maps into memory at runtime.
It uses:

- initialized and uninitialized global variables
- heap allocation with a pointer
- stack allocation inside functions
- recursion to show repeated stack-frame creation

Project files:

- `1. Program_Anatomy_Explorer/main.cpp`: demo program
- `1. Program_Anatomy_Explorer/README.md`: project-specific notes
- `1. Program_Anatomy_Explorer/theory.md`: theory summary
- `1. Program_Anatomy_Explorer/interview_helper.md`: quick interview review
- `1. Program_Anatomy_Explorer/program_anatomy_revision.md`: revision guide

## Repository structure

```text
ai-systems-runtime-lab/
|-- README.md
`-- 1. Program_Anatomy_Explorer/
    |-- main.cpp
    |-- program.exe
    |-- README.md
    |-- theory.md
    |-- interview_helper.md
    `-- program_anatomy_revision.md
```

## How to run the current project

If the bundled executable is already present, run:

```powershell
& ".\1. Program_Anatomy_Explorer\program.exe"
```

To compile from source with `g++`:

```powershell
g++ '.\1. Program_Anatomy_Explorer\main.cpp' -o '.\1. Program_Anatomy_Explorer\program.exe'
& ".\1. Program_Anatomy_Explorer\program.exe"
```

## What you will observe

When you run the program, it prints addresses associated with:

- initialized and uninitialized global variables
- dynamically allocated heap memory
- recursive function-local values on the stack

Those outputs help illustrate the separation between data, BSS, heap, and
stack memory regions.

## Next direction

This repository starts with core systems anatomy first. Future projects can
build on that foundation to explore runtime behavior that matters directly for
AI systems, such as memory pressure, execution scheduling, and performance
tradeoffs.
