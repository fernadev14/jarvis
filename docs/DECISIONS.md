# Architecture Decisions

## ADR-001

Use a single OpenResourceAction instead of one action per resource type.

Reason:

The user always performs the same verb:

Open something.

---

## ADR-002

Use Platform abstraction.

Reason:

The rest of the application must never know if it is running on Linux, Windows or macOS.

---

## ADR-003

Knowledge must be data-driven.

Reason:

Applications, websites and future resources should be defined in YAML instead of code.

---

## ADR-004

Local AI first.

Reason:

Jarvis should work completely offline whenever possible using Ollama.