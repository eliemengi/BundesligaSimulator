# Bundesliga ML Simulator · Blazor / C# / ML

![C#](https://img.shields.io/badge/C%23-239120?logo=c-sharp&logoColor=white)
![.NET](https://img.shields.io/badge/.NET-8-512BD4?logo=dotnet&logoColor=white)
![Blazor](https://img.shields.io/badge/Blazor-512BD4?logo=blazor&logoColor=white)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)
[![License](https://img.shields.io/github/license/your-username/your-repo)](./LICENSE)

A hands-on **Bundesliga match & season simulator** built with **Blazor** (UI), **C#** (logic) and **simple ML/probability modeling** under the hood.  
Two modes: **Single Match** and **Full Season** simulation. UI is already implemented; logic is iteratively refactored from a first, working prototype into clean, testable classes.

---

## Why this project?

- I wanted a **real, end-to-end app** that blends **clean UI** with **practical simulation logic** for football.  
- It’s intentionally beginner-friendly in structure (start simple → refactor into proper domain classes), while still teaching **probabilities, matrices, and basic model calibration**.

---

## Features (current)

- **Single Match** simulation (choose Home/Away/Neutral and teams).  
- **Season Simulation** scaffolding (league, year, N simulations), UI wired and ready.  
- **Working Blazor UI** with responsive layout (HTML/CSS) and clean components.  
- **Deterministic or random seeds** for reproducible runs (dev/debug convenience).  
- Gradual extraction of logic into dedicated classes (see “Project Structure”).

---

## Where is the main code?

- **Primary UI + orchestration:** `Pages/HomeWeather.razor`  
  This component currently wires up the inputs, runs the simulation, and renders results.  
  As the project evolves, computational logic migrates into dedicated classes (below).

---

## Project structure (high-level)


> **Note:** The UI is complete. The initial prototype logic lived inside `HomeWeather.razor` to iterate fast; it’s now being **refactored into `/Core`** so the codebase becomes clean, testable, and reusable.  
> **CI/CD & Docker:** The project uses GitHub Actions for continuous integration and delivery. Every commit is automatically built, tested, and published as a ready-to-run Docker image. This makes the simulator instantly deployable on **Windows 🪟, macOS 🍏, and Linux 🐧** without manual setup.

---

## How it works (short version)

1. **Inputs → MatchProps**  
   Home team, away team, venue (home/away/neutral), optional form multipliers, and any manual probability tweaks.

2. **Team baseline**  
   Basic **attack/defense strength** per team (initially static/hand-tuned, later fed by API or precomputed ratings).

3. **Probability model**  
   Start simple (e.g., home-advantage offset + form factor), then iterate toward **Poisson-style goal models** or a calibrated logistic for outcomes (Win/Draw/Loss).

4. **Simulation loop**  
   - **Single Match:** sample or compute expected score/outcome once (or N times and aggregate).  
   - **Season:** iterate matchdays, accumulate table, then compute distribution of standings over many runs.

5. **Results**  
   Return a `MatchResult` / season table with goals, winner, and summary stats. The UI renders neat cards/sections from that.

---

## Tech stack

- **Frontend:** Blazor (Razor components), HTML, CSS (custom, no framework lock-in).  
- **Language:** C# (.NET 8).  
- **Data / ML (iterative):** probability models first; upgrade path to matrix methods and Poisson goal models; optional xG-style calibrations.  
- **API (planned):** **OpenLigaDB** for real teams, fixtures, badges; the simulation logic stays **decoupled** from the API client.  
- **DevOps:** Docker + GitHub Actions CI/CD for automated builds, tests, and cross-platform deployment (Windows 🪟, macOS 🍏, Linux 🐧).

---

## Roadmap (next steps)

- Extract all computation from `Pages/HomeWeather.razor` into `/Core` classes (see structure above).  
- Add **OpenLigaDB** client and map real fixtures/teams.  
- Introduce **Poisson goal models** and/or calibrated logistic for W/D/L.  
- Deterministic **unit tests** in `/Tests` (seeded RNG).  
- Optional: export results as CSV/JSON for analysis.  
- **CI/CD extension:** automatic Docker image publishing (done) + optional deploy to live demo hosting.  

---

## Getting started

**Requirements**
- .NET 8 SDK (or the version in your `.csproj`).
- (Optional) A modern browser (Blazor runs client/server depending on template).
- (Alternative) Docker installed (Windows 🪟, macOS 🍏, Linux 🐧).

**Run manually**

🪟 Windows (PowerShell / CMD)
docker pull ghcr.io/eliemengi/bundesliga-sim-ui:latest
docker run -p 8080:80 ghcr.io/eliemengi/bundesliga-sim-ui:latest
start http://localhost:8080

---
🍏 macOS (Terminal)

docker pull ghcr.io/eliemengi/bundesliga-sim-ui:latest
docker run -p 8080:80 ghcr.io/eliemengi/bundesliga-sim-ui:latest
open http://localhost:8080

---

🐧 Linux (bash / zsh)

docker pull ghcr.io/eliemengi/bundesliga-sim-ui:latest
docker run -p 8080:80 ghcr.io/eliemengi/bundesliga-sim-ui:latest
xdg-open http://localhost:8080   # oder manuell im Browser öffnen
```bash
# from the solution directory
dotnet restore
dotnet build
dotnet run




