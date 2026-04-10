# Theory Notes

## Compilation vs Linking
Compilation converts source code to object code.
Linking combines object files into an executable.

## Process Image
Includes:
- Code
- Data
- Heap
- Stack

## Virtual Memory
Each process has its own virtual address space managed by the OS.

## Loader Role
The OS loader:
- Loads executable into memory
- Sets up stack and heap
- Starts execution

## Memory Segments Deep Dive
Text: read-only instructions
Data: initialized globals
BSS: uninitialized globals
Heap: dynamic memory
Stack: function execution
