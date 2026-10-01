---
layout: research
title: PatchBudget
subtitle: Candidate verification under a fixed test-query budget
excerpt: A controlled QuixBugs mutation study of test allocation, useful coverage, and false acceptance under a fixed verification budget.
permalink: /research/patchbudget/
order: 4
published: true
featured: false
supervisors: []
tags: [Python, Software testing, Test allocation, NumPy, Matplotlib, Reproducible experiments]
image: ''
image_alt: ''
repository_name: patchbudget
repository_url: https://github.com/KrishnaVarun02/patchbudget
demo_url: ''
---

PatchBudget studies how candidate verification policies allocate a fixed number of test queries. It uses controlled QuixBugs mutations and reference oracles to compare accepted-candidate coverage with the risk of accepting candidates that fail held-out tests.

## Implementation and evidence

- Python components for benchmark adapters, candidate execution, and allocation policies.
- Preparation, analysis, and verification scripts with retained outcome matrices and policy selections.
- An experiment covering 241 candidates across 16 algorithms, accompanied by a protocol and LaTeX research-report draft.

## Reported finding

With 32 additional test queries and eight required passing probes, the repository reports **93.13% useful coverage and 3.75% false acceptance** for focused allocation, compared with **62.08% and 1.46%** for round robin. Useful coverage counts accepted candidates that agree with every held-out test; it does not prove correctness. The results show a coverage–risk trade-off influenced by the acceptance threshold.

## Scope

One budget unit reveals one candidate/test outcome; outcome-matrix construction, oracle generation, and the shared developer gate are accounted for separately. This AI-assisted, reference-oracle study evaluates benchmark mutants. AI-generated patches and repository-scale repair were not evaluated, and the manuscript has no recorded submission, peer review, or acceptance.
