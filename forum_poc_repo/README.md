# Forum-Catalog PoC

This Proof-of-Concept repository contains a minimal project skeleton for a Forum-Catalog of shops:
- Backend: Django + Django REST Framework (skeleton)
- Frontend: Next.js placeholder (pages and API routes)
- Docker Compose setup for local development (web, db, redis)
- CI: GitHub Actions workflow for tests
- Issues: GitHub Issues as markdown for task breakdown
- Wireframes: simple PNG wireframes for main pages

## How to run (dev)
1. Install Docker & Docker Compose.
2. From repository root:
   ```bash
   docker-compose up --build
   ```
3. Backend (Django) service will be available (ports configured in docker-compose).

This PoC is intended for rapid iteration. Implementations are minimal; the goal is to provide a concrete starting scaffold.

---
## Quick Deploy to Render (Free Tier)
Click the button below to deploy the forum PoC automatically on Render:
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/USERNAME/REPO)
*Replace `USERNAME/REPO` with your GitHub repository path after import.*

After deployment, your backend, frontend, and database will be live automatically.
