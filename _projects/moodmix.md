---
layout: project
title: MoodMix
subtitle: Mood-Aware Multilingual Spotify Playlists
excerpt: A playlist application that combines mood and song-language preferences with a durable workflow for creating Spotify playlists.
project_slug: moodmix
permalink: /projects/moodmix/
order: 4
published: true
featured: false
supervisors: []
tags: [Next.js, TypeScript, Tailwind CSS, PostgreSQL, Spotify API, OAuth, Docker]
project_date: ''
image: ''
image_alt: ''
repository_url: 'https://github.com/KrishnaVarun02/moodmix'
demo_url: ''
---

MoodMix is a full-stack playlist application built around a listener's mood and preferred song languages. It combines a Next.js interface with PostgreSQL and a separate durable worker to manage playlist-generation jobs.

## Playlist workflow

- Collects mood, song-language preferences, favorite artists, playlist length, and explicit-content preferences.
- Uses a configurable language-model endpoint for validated mood interpretation and ordered song candidates.
- Checks independent language evidence, searches Spotify, validates track and artist matches, and removes duplicate or unavailable tracks.
- Connects Spotify accounts through OAuth with PKCE and state validation, encrypted tokens, and server-side sessions.

## Durable execution

PostgreSQL job leases, per-user locks, fencing tokens, and idempotent submission coordinate the worker. Checkpoints preserve progress, while bounded retries and reconciliation handle rate limits and uncertain playlist writes.

The application includes account-scoped history, disconnection, and application-data deletion. Model inputs and intermediate plans are encrypted, with lifecycle-based cleanup.

## Integration status

The repository includes the application, migrations, automated checks, and deployment instructions. Live Spotify verification remains pending and requires real authorization and an approved model service. The starter language catalog is intentionally small, so playlist requests can return fewer songs than requested.
