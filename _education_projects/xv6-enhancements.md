---
layout: education_project
title: xv6 Enhancements
excerpt: Virtual memory, kernel threads, scheduling, and observability extensions to MIT's RISC-V xv6.
permalink: /education/projects/xv6-enhancements/
project_slug: xv6-enhancements
order: 5
published: true
featured: false
tags: [C, RISC-V, xv6, Operating systems, QEMU]
repository_url: https://github.com/KrishnaVarun02/xv6-enhancements
demo_url: ''
image: ''
image_alt: ''
---

This project extends MIT's RISC-V xv6 with virtual memory, kernel threads, scheduling policies, and process monitoring. It retains the upstream code's provenance and MIT license.

## Kernel features

- Demand-zero `sbrk` allocates physical pages on access, with shared fault handling for user accesses and kernel copy operations.
- Anonymous `mmap` supports read-only and read-write protection, lazy population, private fork copies, and whole-region unmapping.
- `clone` and `join` create independently scheduled tasks sharing an address space, with separate registers and stacks.
- Runtime policy selection switches between round-robin and proportional-share stride scheduling.
- Monitoring commands expose task state, dispatches, CPU ticks, and allocation information.

## Validation

Guest regression tests run inside QEMU. They exercise lazy allocation, zero-filled pages, fault handling, fork isolation, memory protection, thread lifetime, pipe communication, and scheduling arguments. The host harness detects assertions, kernel panics, unexpected exits, and timeouts.

## Project scope

The repository describes a new implementation of coursework features built on a pinned upstream xv6 revision. The kernel remains an educational system: mappings are anonymous, and address-space layout changes are restricted while threads have unjoined siblings. The repository documents these constraints alongside its design and validation notes.
