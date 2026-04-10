# Program Anatomy Explorer - README

## Overview
This project helps understand how a program runs at a systems level.

## Key Concepts

### What is a Process?
A process is a running instance of a program with its own memory space, execution context, and OS-managed resources.

### Memory Layout
- Text Segment: compiled instructions
- Data Segment: initialized globals
- BSS Segment: uninitialized globals
- Heap: dynamic memory
- Stack: function calls and locals

### Stack vs Heap
Stack:
- Fast allocation
- Function scoped
- Managed automatically

Heap:
- Dynamic allocation
- Flexible lifetime
- Requires manual/runtime management

## Observations
- Global initialized → Data segment
- Global uninitialized → BSS
- Local variables → Stack
- Dynamic allocation → Heap
- Instructions → Text segment

## Why this matters
Understanding this helps in debugging memory issues, performance optimization, and system design.
