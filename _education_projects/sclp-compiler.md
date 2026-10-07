---
layout: education_project
title: SCLP Compiler
excerpt: A typed C-subset compiler with three-address code, register-transfer IR, and native assembly generation for AArch64 and x86-64.
permalink: /education/projects/sclp-compiler/
project_slug: sclp-compiler
order: 2
published: true
featured: false
tags: [C++17, Flex, Bison, Compilers, AArch64, x86-64]
repository_url: https://github.com/KrishnaVarun02/sclp-compiler
demo_url: ''
image: ''
image_alt: ''
---

SCLP is a compiler for a small, statically typed C-like language, built with Flex, Bison, and C++17. It emits native assembly for AArch64 macOS and x86-64 Linux, linking generated programs against a small C runtime.

## Compiler pipeline

- Parses typed functions, local variables, lexical scopes, and control flow.
- Produces three-address code and lowers it to an explicit register-transfer intermediate representation.
- Applies basic-block constant propagation and constant folding with the optional optimization pass.
- Emits target-specific assembly with function prologues, stack frames, and register argument passing.

## Language and validation

The language supports integers and booleans, recursion, conditionals, loops, early returns, and short-circuit Boolean expressions. Source-line diagnostics identify invalid programs, while runtime checks handle division errors.

The repository includes end-to-end compilation and execution tests, rejection tests for invalid programs, checks of intermediate representations, and cross-assembly checks when Clang is available.

## Project scope

The repository documents this as a contemporary educational reconstruction inspired by a university compiler project. It is an independent compiler with its own educational IR. Its deliberately small language excludes features such as pointers, arrays, floating point, and general C compatibility.
