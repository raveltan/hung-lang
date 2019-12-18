# Hung Programming Language
## What is Hung?
Hung is a programming langguage cerated by [Ravel Tanjaya](https://www.instagram.com/raveltan) written in python, this programming language can be compiled to machine code. Hung uses LLVM and GCC in order to convert it's code to an executeable machine code.

### Why Create Hung?
For poeple who might be new to programming, choosing the right programming language can be quite a hassle, especially when considering that certain programming languages are build to be use with certain purpose. That's why we create Hung.<br>

Hung is created to help people to learn programming concept and we hope that hung can be adopted for wider use in the future.

## Current State
Hung are currently available as technology preview. We have not even reach alpha which means the code can be highly unstable.

## Installation Guide
>There are currently no easy way to install Hung, and only installation on Unix based systems are tested (Linux & Mac OS)

### Requirements
In order for Hung to be run on certain machine please make sure that these depedencies are satisfied:
1. Anconda (Python 3.7)
2. LLVMlite
3. RPLY
4. LLC (LLVM static compiler)
5. GCC 

### Install & Compile (UNIX)
Clone The Git Repo to your local machine and go inside the clone folder
```bash 
git clone https://github.com/raveltan/hung-lang.git
cd hung-lang
```
File.hung is the file that is going to be compiled to machine code.
Edit this file and save it
To compile your code, run this following command
```bash
python3 main.py
```
A new file called output will be available on the output folder, this is the generated executable

## Known Bugs
TBA

## Unimplemented Features
TBA

