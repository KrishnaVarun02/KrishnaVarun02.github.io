---
layout: project
title: Parvathi
subtitle: Native Voice Assistant for Windows and macOS
excerpt: A native desktop voice assistant for dictation, validated computer commands, and spoken conversation on Windows and macOS.
project_slug: parvathi
permalink: /projects/parvathi/
order: 3
published: true
featured: false
supervisors: []
tags: [Swift, SwiftUI, AppKit, "C#", WPF, Vosk, Apple Speech, Ollama]
project_date: ''
image: ''
image_alt: ''
repository_url: 'https://github.com/KrishnaVarun02/Parvathi'
demo_url: ''
---

Parvathi is a native desktop voice assistant for dictation into other applications, a defined set of computer commands, and questions with spoken replies. Separate Dictation, Command, and Ask modes make the intended action explicit.

## Voice interaction

- Supports push-to-talk dictation, spoken questions, and commands for opening applications or websites, web searches, and audio controls.
- Provides optional AI-assisted text polishing, rewriting, and explanations through a configured OpenAI or Ollama provider.
- Routes recognized commands through typed actions and validation. Model-generated text cannot execute arbitrary computer commands.

## Native platform integration

The Windows application uses C# and WPF with offline Vosk speech recognition. The macOS application uses SwiftUI and AppKit with Apple Speech, Accessibility, CoreAudio, and Keychain.

On macOS, text insertion checks the destination application, field, and selection before applying an edit. Its clipboard fallback preserves newer clipboard changes, while cancellation stops pending recognition, requests, and speech.

## Project status

The repository includes native applications, automated checks, packaging scripts, and platform documentation. Windows is available as a prerelease; live microphone, cross-application, and authenticated-provider acceptance checks remain documented separately from build and automated test results.
