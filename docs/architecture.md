# Architecture

## Overview

Jarvis AI is a modular AI assistant designed to run locally using Ollama.

The project is organized around independent layers, where each module has a single responsibility.

```
User
   │
   ▼
Console / Voice / API
   │
   ▼
Assistant
   │
   ├──────────────┐
   ▼              ▼
Brain            NLU
                  │
                  ▼
          Knowledge Registry
                  │
                  ▼
            Action Router
                  │
                  ▼
               Actions
                  │
                  ▼
              Platform
                  │
      ┌───────────┴───────────┐
      ▼           ▼           ▼
    Linux      Windows      macOS
```

---

## Modules

### Assistant

Coordinates the entire system.

### Brain

Communicates with the language model.

### NLU

Transforms user text into structured understanding.

### Knowledge

Stores information about applications, websites, folders and future resources.

### Action Router

Chooses which action should be executed.

### Actions

Execute the requested operation.

### Platform

Interacts with the operating system.

---

## Design Principles

- Single Responsibility
- Dependency Injection where appropriate
- Modular architecture
- Platform abstraction
- Local-first AI
- Extensible through plugins