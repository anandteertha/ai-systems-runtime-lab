# Program Anatomy Explorer -- Revision Guide

## What this project demonstrates

This project shows how a C++ program is represented in memory when it
runs.

## Program vs Process

Program: static file on disk\
Process: running instance with memory + resources

## Memory Layout

-   Text: instructions
-   Data: initialized globals
-   BSS: uninitialized globals
-   Heap: dynamic allocation
-   Stack: function calls and locals

## Key Observations

-   Globals live together
-   Heap is separate
-   Stack grows with recursion

## Pointer vs Heap

Pointer stores address\
Heap is actual allocated memory

## Stack vs Heap

Stack: fast, automatic\
Heap: flexible, manual

## Recursion

Each call creates a new stack frame

## RAII

Scope-based cleanup via destructors

## Final Insight

Different data lives in different memory regions with different
lifetimes
