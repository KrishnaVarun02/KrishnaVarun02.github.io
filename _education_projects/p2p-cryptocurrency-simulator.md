---
layout: education_project
title: P2P Cryptocurrency Network Simulator
excerpt: A discrete-event model of transaction propagation, proof-of-work mining, forks, and independent selfish miners in a peer-to-peer network.
permalink: /education/projects/p2p-cryptocurrency-simulator/
project_slug: p2p-cryptocurrency-simulator
order: 3
published: true
featured: false
tags: [Python, Discrete-event simulation, Blockchain, Peer-to-peer networks]
repository_url: https://github.com/KrishnaVarun02/p2p-cryptocurrency-simulator
demo_url: ''
image: ''
image_alt: ''
---

This standard-library Python simulator models a cryptocurrency network as peers with local block trees, account ledgers, mempools, and information delays. A priority queue advances between transaction, network, and mining events.

## Network and consensus model

- Models message queues, bandwidth, base latency, and jitter across peer links.
- Validates balances and sender nonces against local ledger state, including side branches.
- Handles unknown-parent blocks, forks, chain reorganizations, and restoration of valid transactions to mempools.
- Supports honest mining and independent block-withholding strategies, including two selfish miners with separate private branches.

## Experiments and reporting

Seeded configuration makes runs reproducible. JSON and CSV reporting cover propagation, stale blocks, throughput, inclusion delay, tip agreement, and per-miner revenue. Configuration sweeps compare mining strategies across hash-power allocations and seeds.

Tests cover ledger validation, fork selection, reorganization, private-branch transitions, network queue timing, and deterministic output.

## Project scope

The repository presents a new implementation based on a project description. Reported experiments are simulation outputs. The model uses trusted identities and simplified proof-of-work timing; signatures, variable difficulty, and production consensus rules are outside its scope.
