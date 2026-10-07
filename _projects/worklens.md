---
layout: project
title: WorkLens
subtitle: Contribution Evidence and Workforce Planning
excerpt: A self-hosted application that connects engineering work evidence, skills, and company roadmaps through explainable metrics and human review.
project_slug: worklens
permalink: /projects/worklens/
order: 5
published: true
featured: false
supervisors: []
tags: [Python, Django, React, TypeScript, PostgreSQL, Docker, Jira, Bitbucket, Confluence]
project_date: ''
image: ''
image_alt: ''
repository_url: 'https://github.com/KrishnaVarun02/worklens'
demo_url: ''
---

WorkLens is a self-hosted application for engineering contribution evidence, skills, and workforce planning. It connects structured work records with employee context, human reviews, and explicit company roadmaps.

## Evidence and review

- Provides personal and team dashboards, employee profiles, goals, skills matrices, roadmap gaps, reviews, and corrections.
- Uses deterministic calculations across seven explainable dimensions, with versioned formulas, frozen inputs, source freshness, sample sizes, and evidence links.
- Retains original evidence alongside correction approvals and append-only assessments.
- Supports authorized CSV and PDF reporting with role-based access and audit records.

## Integrations and architecture

The React and TypeScript interface is backed by Django and PostgreSQL. Separate Jira, Bitbucket, and Confluence adapters support resumable synchronization, identity-resolution review, and CSV imports.

Deployment tooling includes HTTPS Docker Compose configuration, encrypted connector credentials, controlled outbound networking, and authenticated encrypted backups. A separate worker processes synchronization and report jobs.

## Decision support and verification

WorkLens supports human review of documented contributions and skills. It does not calculate employee rankings or automate hiring, firing, promotion, or compensation decisions. Missing observations remain explicitly unknown.

The repository includes synthetic demonstration data and automated API, connector, metric, and browser checks. Source adapters are fixture-tested; verification against a live customer tenant is not claimed.
