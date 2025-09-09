# Bundesliga ML Simulator · Blazor / C# / ML / Docker CI/CD

![C#](https://img.shields.io/badge/C%23-239120?logo=c-sharp&logoColor=white)
![.NET](https://img.shields.io/badge/.NET-8-512BD4?logo=dotnet&logoColor=white)
![Blazor](https://img.shields.io/badge/Blazor-512BD4?logo=blazor&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

A machine learning based Bundesliga simulator that predicts match outcomes and full league seasons.  
Built with **C#**, **Blazor** and statistical models, featuring both **single-match** and **season** simulations.  
The project is fully integrated with **Docker-based CI/CD** using **GitHub Actions** – every commit is automatically built, tested, and published as a ready-to-run Docker image.  

This means: **no manual setup, no dependency hell** – anyone can run the simulator on **Windows**, **macOS**, or **Linux** in seconds with Docker.  
Perfect for showcasing DevOps practices (CI, CD, containerization) alongside C# and Blazor development.

---

## 🚀 Quickstart with Docker (choose your OS)

Thanks to CI/CD, the Docker image is always up to date. Pull & run it on your system:

---

### 🪟 Windows (PowerShell / CMD)

```powershell
# 1) Pull the latest image from GitHub Container Registry (GHCR)
docker pull ghcr.io/eliemengi/bundesliga-sim-ui:latest

# 2) Run the container, map port 8080 to localhost
docker run -p 8080:80 ghcr.io/eliemengi/bundesliga-sim-ui:latest

# 3) Open the app in your browser
start http://localhost:8080
🍏 macOS (Terminal)
bash
Code kopieren
# 1) Pull the latest image
docker pull ghcr.io/eliemengi/bundesliga-sim-ui:latest

# 2) Run the container
docker run -p 8080:80 ghcr.io/eliemengi/bundesliga-sim-ui:latest

# 3) Open in Safari / default browser
open http://localhost:8080
🐧 Linux (bash / zsh)
bash
Code kopieren
# 1) Pull the latest image
docker pull ghcr.io/eliemengi/bundesliga-sim-ui:latest

# 2) Run the container
docker run -p 8080:80 ghcr.io/eliemengi/bundesliga-sim-ui:latest

# 3) Open in your browser
xdg-open http://localhost:8080   # or open manually
✅ After this, the simulator runs locally at http://localhost:8080 on any platform.
This demonstrates a full DevOps pipeline: CI (build & test) + CD (publish Docker image) → seamless developer and user experience.

🎯 Why this project?
A real, end-to-end app blending clean UI with practical football simulation logic.

Beginner-friendly structure: start with simple logic, then refactor into proper domain classes.

Demonstrates DevOps readiness: CI/CD pipelines, Docker containerization, reproducibility.

Teaches probability models, matrices, and model calibration along the way.

Built as a showcase project for software engineering, DevOps, and applied machine learning.

✨ Features
Single Match simulation: choose Home/Away/Neutral, teams, and get outcome probabilities.

Season Simulation scaffolding: simulate an entire league with many runs.

Modern Blazor UI with responsive layout and clean components.

Deterministic or random seeds for reproducible runs.

Refactoring in progress: logic is moving into clean, testable core classes.

Docker-ready: containerized, portable, identical runs everywhere.

CI/CD integration: automatic builds & published Docker image with every push.

🗂 Project structure
UI + orchestration: Pages/Home.razor

Core logic (refactor target): /Core

Docker configuration: BundesligaSimulator/Dockerfile, nginx.conf, .dockerignore

CI/CD pipelines: .github/workflows/ci.yml (build), .github/workflows/cd.yml (publish to GHCR)

⚙️ How it works
Inputs → MatchProps (teams, venue, form multipliers).

Team baseline → attack/defense strengths (static, later via API).

Probability model → start with simple offsets, expand to Poisson/logistic models.

Simulation loop → single match OR full season iterations.

Results → predicted goals, outcome, season standings.

🛠 Tech stack
Frontend: Blazor, HTML, CSS

Language: C# (.NET 8)

Models: simple probability → Poisson/logistic

API (planned): OpenLigaDB (real fixtures, teams, logos)

DevOps: GitHub Actions (CI/CD), Docker, GHCR

Hosting (planned): Render / Azure for live deployment

📌 Roadmap
✅ Refactor computation into /Core classes

✅ Add Dockerfile + nginx.conf + dockerignore

✅ GitHub Actions CI (build, test, publish)

✅ GitHub Actions CD (push Docker image to GHCR)

🔜 Add OpenLigaDB API client (real fixtures/teams)

🔜 Implement Poisson models for goal distribution

🔜 Add unit testing suite (xUnit)

🔜 Export results as CSV/JSON

🔜 Optional: Auto-deploy to Render/Azure with live URL

▶️ Getting started (manual run without Docker)
For developers who want to run locally without Docker:

Requirements: .NET 8 SDK, Browser

bash
Code kopieren
dotnet restore
dotnet build
dotnet run
Then open http://localhost:5000 (or the port shown in terminal).

✅ Summary
This project is both a football simulator and a DevOps case study:

Built with C# / Blazor for modern frontend.

Uses ML-inspired statistical models for simulation.

Packaged with Docker for platform independence.

Fully automated CI/CD pipelines ensure every push delivers a fresh, working Docker image.

Perfect for showing skills in software engineering, DevOps, and applied data science.

yaml
Code kopieren

---

Das ist jetzt ein richtig ausführlicher, sauber strukturierter, professioneller README – alles in **einem Markdown-Block**, mit extra OS-Blöcken (Windows → macOS → Linux in der Reihenfolge) und klarer Betonung auf **CI, CD, Docker**.  

👉 Soll ich dir auch gleich noch einen **Badge einbauen, der direkt auf dein Docker-Image in GHCR verlinkt**, sodass im Header sofort „Docker Pull“ steht?







ChatGPT fragen
