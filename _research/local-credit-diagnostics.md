---
layout: research
title: Local Credit Diagnostics
subtitle: When Local Credit Assignment Breaks
excerpt: An executed synthetic study of reward reconstruction error, additive and pairwise projections, and cooperative decision quality.
permalink: /research/local-credit-diagnostics/
order: 3
published: true
featured: false
supervisors: []
tags: [Python, NumPy, Cooperative decision-making, Reward decomposition, Reproducible experiments]
image: ''
image_alt: ''
repository_name: local-credit-diagnostics
repository_url: https://github.com/KrishnaVarun02/local-credit-diagnostics
demo_url: ''
---

Local Credit Diagnostics examines how reward reconstruction error relates to cooperative decision quality. Exact additive and pairwise reward projections in synthetic games make it possible to inspect both prediction error and coordination regret.

## Implementation and evidence

- Python implementations of games, feature spaces, projections, and evaluation metrics.
- Tests comparing analytical formulas with least-squares solutions.
- A documented protocol, retained experiment results, reproduction tools, and a LaTeX manuscript draft.
- The repository records 96 exact evaluations and 800 finite-coverage fits.

## Reported finding

In the supplied 16-agent sparse-synergy game, the additive fit has raw MSE **0.0000152548** and coordination regret **0.999268**. Its MSE divided by reward variance is **0.999939**, showing why the small raw error does not establish strong predictive accuracy. Adding pairwise factors reduces error while leaving the selected maximizing action unchanged in this setting.

## Scope

This is an AI-assisted synthetic diagnostic study with a manuscript awaiting author and scientific review. It examines an established limitation of reward projection; neural MARL reproduction and sequential external benchmark validation were not performed. The repository records no academic submission, peer review, or acceptance.
