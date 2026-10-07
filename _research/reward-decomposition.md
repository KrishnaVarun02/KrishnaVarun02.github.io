---
layout: research
title: Reward Decomposition in MARL — LOMAQ
excerpt: Undergraduate study of structural credit assignment, monotonic value decomposition, and decentralized execution in cooperative multi-agent reinforcement learning.
permalink: /research/reward-decomposition/
order: 1
published: true
featured: true
supervisors: [Dr. Lakshmanan Kailasam]
tags: [Multi-agent reinforcement learning, LOMAQ, CTDE, Reward decomposition, PyTorch]
image: ''
image_alt: ''
repository_name: Reward-Decomposition-in-MARL-LOMAQ
repository_url: https://github.com/KrishnaVarun02/Reward-Decomposition-in-MARL-LOMAQ
demo_url: ''
---

## Overview

This undergraduate research project studies cooperative **multi-agent reinforcement learning (MARL)** through the LOMAQ reward-decomposition framework. The focus is structural credit assignment: how decomposing a team objective into local and partition-level rewards can support centralized training while retaining decentralized action selection.

## Research Focus

The study examines whether a monotonic value-decomposition formulation can represent partition-level reward structure while preserving the consistency required for decentralized greedy execution.

## Methodology

- Independent per-agent utility networks map neighborhood-local observations to action utilities.
- Monotonic partition mixers combine the full vector of agent utilities for each reward partition.
- Positive mixer weights and increasing activations enforce monotonicity structurally.
- Centralized training uses replay, Double-DQN target selection, periodically updated target networks, Adam optimization, and gradient clipping.
- A compact **Linked Navigation** environment models cooperative movement with coupled neighboring agents and a finite horizon.
- QMIX, VDN, IQL, and IQL-local are implemented as comparison methods under matched environment, network, optimizer, exploration, and evaluation settings.

## Experiments / Evaluation

The repository provides executable training and evaluation workflows, configuration validation, automated tests, checkpoint persistence, and deterministic CPU execution. The validation suite tests decentralized action independence, additive reward locality, monotonic gradients, terminal masking, replay persistence, and exact interrupted/resumed training.

A controlled smoke evaluation uses 250 training episodes, 4,000 environment steps, and disjoint evaluation reset seeds. The reported evaluation contains 32 episodes for each method.

## Results / Findings

In the recorded smoke evaluation, LOMAQ achieved a **mean team return of 14.333** and **100% final joint-goal success**. The same evaluation reports 14.367 for QMIX, 14.244 for IQL, 14.246 for IQL-local, and 14.222 for VDN.

These measurements demonstrate executable learning and validation on the repository's compact task; they are not presented as evidence of general superiority across MARL benchmarks.

The repository also explicitly separates these executable experiments from the historical project report: the original report's numerical experiments are not claimed to have been reproduced because the required historical environments, checkpoints, configurations, and raw logs are not preserved.

## Technical Details

**Python · PyTorch · NumPy · pytest · Ruff · Double DQN · replay learning · monotonic value mixing · CTDE**

The repository includes configuration files, source code, tests, validation metrics, checkpoint/resume support, and the original project report.

## Limitations

The current executable experiments use a small custom cooperative environment rather than a standard large-scale MARL benchmark. The repository therefore supports methodological and implementation analysis, but not broad claims about performance across cooperative MARL tasks.

## Repository

[Reward-Decomposition-in-MARL-LOMAQ](https://github.com/KrishnaVarun02/Reward-Decomposition-in-MARL-LOMAQ)
