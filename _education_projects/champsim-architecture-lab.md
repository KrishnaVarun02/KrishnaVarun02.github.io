---
layout: education_project
title: ChampSim Architecture Lab
excerpt: A branch prediction and cache replacement lab with native ChampSim modules and reproducible synthetic experiments.
permalink: /education/projects/champsim-architecture-lab/
project_slug: champsim-architecture-lab
order: 4
published: true
featured: false
tags: [C++17, Python, ChampSim, Branch prediction, Cache replacement]
repository_url: https://github.com/KrishnaVarun02/champsim-architecture-lab
demo_url: ''
image: ''
image_alt: ''
---

ChampSim Architecture Lab combines an L-TAGE-style branch predictor, loop prediction, and cache replacement policies in a C++17 lab. Native modules integrate the implementations with a pinned ChampSim revision.

## Prediction and replacement

- Uses geometric history lengths, tagged predictor banks, provider selection, useful-bit aging, and deterministic allocation.
- Adds a loop predictor that learns iteration counts and confidence before overriding the base prediction.
- Implements LRU, LFU with LRU tie breaking, and insertion-based FIFO replacement.
- Provides standalone functional models alongside native simulator adapters.

## Experiment workflow

The repository contains deterministic workload generation, configuration sweeps, IPC and MPKI extraction, and a train/validation/test workflow for externally supplied traces. Tests cover eviction ordering, predictor learning, determinism, trace validation, and metric extraction.

## Project scope

This is a new implementation based on an architecture-project brief. Its checked-in results use 16 small synthetic workloads. SAT-solver performance and results on large application traces are not established by those experiments. The predictor emphasizes readable implementation and makes no hardware area or timing claims.
