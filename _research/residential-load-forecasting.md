---
layout: research
title: Short-Term Residential Load Forecasting Using Deep Learning
excerpt: Undergraduate study of recurrent neural networks for short-term residential electricity-load forecasting with chronological evaluation and controlled preprocessing.
permalink: /research/residential-load-forecasting/
order: 2
published: true
featured: true
supervisors: [Prof. S. K. Singh, Dr. Jayashankara M]
tags: [Deep learning, LSTM, GRU, Time-series forecasting, PyTorch, scikit-learn]
image: ''
image_alt: ''
repository_name: Residential-Load-Forecasting-with-LSTM
repository_url: https://github.com/KrishnaVarun02/Residential-Load-Forecasting-with-LSTM
demo_url: ''
---

## Overview

This undergraduate research project investigates **short-term residential electricity-load forecasting** using recurrent neural networks, with particular attention to LSTM and GRU architectures and to the experimental choices that affect time-series evaluation.

## Research Focus

The project examines how recurrent models compare with simpler forecasting approaches when the temporal ordering of observations is respected, and how preprocessing and evaluation design influence reported forecasting performance.

## Methodology

- LSTM and GRU recurrent architectures are evaluated alongside linear, Ridge, Lasso, polynomial, persistence, and empirical forecasting baselines.
- Data are divided chronologically into training, validation, and test periods.
- Feature filling, normalization ranges, and model-selection decisions are fitted using training information rather than future test observations.
- Temporal windows crossing timestamp gaps are excluded.
- The best neural checkpoint is selected using validation loss before final test evaluation.
- Saved preprocessing and model artifacts support model reload and next-interval inference.

## Experiments / Evaluation

The repository contains the original project materials together with a maintained executable forecasting workflow. The committed daily series contains 1,442 daily observations. The evaluation reports RMSE, MSE, MAE, R², explained variance, WAPE, and MAPE, with explicit handling for zero and constant targets.

The maintained daily pipeline provides a leakage-aware comparison across the recurrent and non-neural baselines.

## Results / Findings

On the committed daily evaluation, the test **R² is 0.250 for LSTM and 0.396 for Ridge**. These results are useful as a controlled comparison within the maintained dataset and protocol rather than as a claim that a neural model universally outperforms simpler baselines.

The preserved project report also contains a GRU experiment with **R² = 0.938 and RMSE = 0.263**; these figures are retained as report results and are distinct from the maintained daily evaluation protocol.

## Technical Details

**Python · PyTorch · scikit-learn · pandas · NumPy · LSTM · GRU · regression baselines · chronological time-series evaluation**

The repository includes preprocessing, model definitions, metrics, configuration, tests, saved-artifact evaluation, and inference workflows.

## Limitations

The maintained evaluation is based on a single-household residential load series. Results should therefore be interpreted within the dataset and forecasting protocol rather than generalized to other households or forecasting settings.

## Repository

[Residential-Load-Forecasting-with-LSTM](https://github.com/KrishnaVarun02/Residential-Load-Forecasting-with-LSTM)
