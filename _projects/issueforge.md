---
layout: project
title: IssueForge
subtitle: Multi-Agent GitHub Issue-to-PR Orchestrator
excerpt: A multi-agent workflow that turns GitHub issues into implementation plans, validated patches, regression tests, and human-approved pull requests.
project_slug: issueforge
permalink: /projects/issueforge/
order: 1
published: true
featured: true
tags: [Python, LangGraph, Pydantic, Docker, Git, GitHub API, SQLite, Pytest, OpenRouter]
image: ''
image_alt: ''
repository_url: 'https://github.com/KrishnaVarun02/IssueForge-Multi-Agent-GitHub-Issue-to-PR-Orchestrator'
demo_url: ''
---

IssueForge is a multi-agent coding platform that transforms GitHub issues into implementation plans, validated code patches, regression tests, and human-approved pull requests. It combines a stateful agent workflow with isolated execution and review checkpoints.

## Seven-stage workflow

The LangGraph workflow moves through seven stages:

1. **Code Reader:** examines the relevant code context.
2. **Planner:** prepares an implementation plan.
3. **Code Writer:** produces the proposed changes.
4. **Test Writer:** adds regression tests.
5. **Sandbox execution:** runs and validates the changes in an isolated environment.
6. **Human approval:** supports inspection, feedback, and approval.
7. **PR delivery:** delivers the approved changes as a pull request.

## Reliability and execution controls

- Strict Pydantic schemas, prompt-injection defenses, safe-path validation, and deterministic diffs constrain agent outputs.
- Bounded retries and configurable cost budgets keep execution limits explicit.
- Offline Docker execution applies least-privilege controls, read-only access, and CPU, memory, process, network, and privilege restrictions.
- SQLite checkpointing persists workflow state for inspection, pausing, approval, revisions, failure recovery, and resumable execution.

## Developer workflow integration

The platform integrates GitHub issue ingestion, isolated Git worktrees, automated commits, and authenticated pull-request creation. Execution telemetry and secret-safe reporting make the workflow inspectable through its stages.
