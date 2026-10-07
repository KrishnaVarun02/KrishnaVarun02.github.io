---
layout: research
title: Local Credit Diagnostics
subtitle: Diagnosing reward reconstruction and cooperative decision quality
excerpt: Controlled synthetic study of when reward reconstruction error can fail to reflect cooperative decision quality.
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

## Overview

This undergraduate research-oriented study investigates the relationship between **reward reconstruction error** and **cooperative decision quality**. It asks whether a decomposition that achieves a small numerical reconstruction error necessarily preserves the actions that matter for cooperative decision-making.

## Research Focus

The central research question is whether standard reconstruction metrics are sufficient for evaluating reward decompositions when the downstream objective is selecting high-quality joint actions.

## Methodology

- Constructed fully enumerable synthetic cooperative games with additive and interaction-based feature spaces.
- Evaluated additive and pairwise reward projections using exact population calculations and finite-sample least-squares fits.
- Compared analytical projection formulas against least-squares solutions.
- Measured reconstruction MSE together with normalized error, regret, selected action, and decision success.
- Included controlled variations in agent count, interaction structure, reward strength, and sample coverage.
- Preserved source hashes, configuration files, seeds, generated results, figures, and verification scripts for reproducibility.

## Experiments / Evaluation

The executed study contains **96 exact evaluations and 800 finite-coverage fits** across the documented experimental cells, together with control experiments and an attributed published payoff matrix used only as a sanity check.

The analysis deliberately distinguishes training-data coverage from downstream decision quality and does not treat raw MSE as a sufficient evaluation criterion.

## Results / Findings

In the 16-agent sparse-synergy setting, the additive projection has raw **MSE = 0.0000152548** while **coordination regret = 0.999268**. Normalizing MSE by reward variance gives **0.999939**.

Adding pairwise factors lowers reconstruction error in the reported setting, but the maximizing action remains unchanged. Together, these results illustrate that a small reconstruction error can coexist with poor decision quality.

## Technical Details

**Python · NumPy · exact enumeration · least-squares projection · synthetic cooperative games · reproducible experiment manifests**

The repository includes executable experiment and analysis scripts, tests, configurations, raw result tables, figures, and a manuscript draft documenting the study.

## Limitations

The study is synthetic and diagnostic. It does not reproduce a neural MARL benchmark and does not establish how the observed metric relationship transfers to larger sequential environments.

## Repository

[local-credit-diagnostics](https://github.com/KrishnaVarun02/local-credit-diagnostics)
