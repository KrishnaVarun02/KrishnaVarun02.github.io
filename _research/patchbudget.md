---
layout: research
title: PatchBudget
subtitle: Candidate verification under a fixed test-query budget
excerpt: Controlled study of test allocation, useful coverage, and false acceptance under a fixed verification budget.
permalink: /research/patchbudget/
order: 4
published: true
featured: false
supervisors: []
tags: [Python, Software testing, Test allocation, QuixBugs, Reproducible experiments]
image: ''
image_alt: ''
repository_name: patchbudget
repository_url: https://github.com/KrishnaVarun02/patchbudget
demo_url: ''
---

## Overview

PatchBudget is an undergraduate research-oriented study of **candidate verification under a fixed test-query budget**. It examines how different test-allocation policies distribute limited verification effort and how that allocation affects useful coverage and false acceptance.

## Research Focus

The study asks how verification outcomes change when candidate patches compete for a limited number of test queries, and whether allocating tests differently changes the trade-off between accepting useful candidates and accepting candidates that fail held-out tests.

## Methodology

- Uses controlled QuixBugs mutations and reference oracles as the experimental benchmark.
- Implements round-robin, candidate-focused, failure-count, and failure-history test-allocation policies.
- Separates scheduling decisions from hidden evaluation outcomes.
- Applies prespecified acceptance thresholds and records candidate/test queries explicitly.
- Retains outcome matrices, policy selections, manifests, and generated analysis artifacts for reproduction.

## Experiments / Evaluation

The full experiment evaluates **241 candidates across 16 benchmark programs** under multiple query budgets, developer-test gates, and minimum passing-test thresholds. The analysis reports acceptance coverage, useful coverage, false acceptance, query usage, and sensitivity to verification thresholds.

Useful coverage is defined using held-out tests and therefore represents agreement with the retained benchmark oracle; it is not a formal proof of program correctness.

## Results / Findings

At a budget of **32 additional test queries** and a minimum of **8 passing probes**, the repository reports:

- **Candidate-focused allocation:** 93.13% useful coverage and 3.75% false acceptance.
- **Round-robin allocation:** 62.08% useful coverage and 1.46% false acceptance.

The comparison illustrates a measurable **coverage–risk trade-off**: the policy with higher useful coverage also accepts more candidates that fail the held-out evaluation.

## Technical Details

**Python · QuixBugs · program execution · test allocation · outcome matrices · controlled evaluation · reproducible analysis**

The repository contains benchmark adapters, execution and scheduling code, experimental results, analysis scripts, figures, tests, and protocol documentation.

## Limitations

The benchmark uses controlled mutations and trusted oracle information. The experiment therefore studies verification-policy behavior under a defined protocol rather than end-to-end software-repair quality or security guarantees.

## Repository

[patchbudget](https://github.com/KrishnaVarun02/patchbudget)
