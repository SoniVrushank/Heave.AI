# HEAVE - Personal AI Operating System

**Version**: 0.1.0 (Phase 2 - Repository Scaffolding)  
**Status**: Development  
**Owner**: Vrushh  
**Assistant**: Hirvi 💗

---

## Overview

HEAVE is a personal AI Operating System built exclusively for Vrushh. It combines workspace management, AI assistance (Hirvi 💗), automation, and personal productivity into a single, premium desktop application.

**Key Features:**
- 🧠 Personal AI companion (Hirvi 💗) powered by local models
- 📝 Smart notes with rich formatting
- 📊 Project and task management
- 🔐 Local-first architecture with end-to-end encryption
- 📱 Android companion app for remote access
- ⚡ Fast, responsive interface inspired by Apple Intelligence
- 🔗 MCP integrations for external tools
- 🤖 Automation engine (Python, PowerShell, n8n)

---

## Project Structure

```
HEAVE/
├── src/                    # React frontend (TypeScript)
├── src-tauri/             # Tauri desktop runtime
├── backend/               # FastAPI backend (Python)
├── database/              # Database schema & migrations
├── docs/                  # Documentation (68+ specs)
├── architecture/          # System architecture
├── brand/                 # Design system & assets
├── prompts/               # Hirvi personality & prompts
├── config/                # Configuration
├── automation/            # Automation engine (Phase 4+)
├── memory/                # Memory & knowledge base
├── mcp/                   # MCP integrations (Phase 5+)
└── ...                    # See PHASE_2_SCAFFOLD_COMPLETE.md
```

---

## Quick Start

### Prerequisites
- **Node.js** 20+ (with npm)
- **Python** 3.11+
- **Rust** (for Tauri compilation)
- **Git**

### Setup

1. **Clone & Install**
   ```bash
   cd "C:\Users\Vrushh\Desktop\Heave Fles\HEAVE"
   npm install
   cd backend && pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   cd backend && cp .env.example .env  # Already exists
   ```

3. **Start Development**

   **Terminal 1 - Frontend (Tauri):**
   ```bash
   npm run dev
   ```

   **Terminal 2 - Backend (FastAPI):**
   ```bash
   cd backend && python main.py
   ```

4. **Login**
   - User ID: `vrushh_98`
   - Password: `Vrush@nk09`
   - ✅ You're in!

---

## Development Commands

```bash
# Frontend
npm run dev              # Start Tauri dev server
npm run build            # Build for production
npm run lint             # Check code quality
npm run lint:fix         # Fix linting issues
npm run format           # Format code
npm run type-check       # TypeScript validation
npm test                 # Run tests
npm run test:ui          # Test UI
npm run test:coverage    # Coverage report

# Backend
cd backend
python main.py           # Start FastAPI server
pytest                   # Run tests
black .                  # Format code
flake8 .                 # Lint code

# Both
make dev                 # Start both (requires terminal splitting)
make build               # Build both
make clean               # Clean artifacts
make test                # Run all tests
```

---

## Architecture

### Frontend Stack
- **Framework**: React 19 + TypeScript
- **Desktop**: Tauri 2.0 (Rust-powered)
- **Styling**: Tailwind CSS + Custom design tokens
- **State**: Zustand
- **Testing**: Vitest + React Testing Library
- **Build**: Vite

### Backend Stack
- **Framework**: FastAPI (Python)
- **Database**: SQLite (local-first)
- **ORM**: SQLAlchemy
- **Server**: Uvicorn
- **Testing**: Pytest

### Design System
- **Theme**: Dark mode (default) + Light mode
- **Language**: Apple-inspired, iOS 26 Liquid Glass
- **Color Palette**: Purple brand with neutral grays
- **Typography**: System fonts for optimal performance
- **Components**: Glass-morphism effects with backdrop blur

---

## Current Phase: Phase 2 ✅

**What's Complete:**
- ✅ Project scaffolding (folder structure)
- ✅ Build pipeline (Vite, Tauri, FastAPI)
- ✅ Design system (colors, typography, spacing)
- ✅ Authentication shell (login page)
- ✅ Navigation shell (sidebar, topbar)
- ✅ Dashboard shell (placeholder)
- ✅ Settings shell (theme toggle)
- ✅ Workspace shell (workspace switcher)
- ✅ Database setup (SQLAlchemy + SQLite)
- ✅ API skeleton (health check, auth endpoints)
- ✅ Development tooling (ESLint, Prettier, testing)

**What's Next (Phase 3):**
- ⏳ Real authentication (JWT, password hashing)
- ⏳ Dashboard implementation
- ⏳ Workspace data persistence
- ⏳ Memory engine
- ⏳ Hirvi AI integration
- ⏳ Full component library

See `PHASE_2_SCAFFOLD_COMPLETE.md` for detailed Phase 2 report.

---

## API Documentation

### Base URL
```
http://localhost:8000/api
```

### Health Check
```http
GET /health
```

Response:
```json
{
  "status": "healthy",
  "service": "heave-backend",
  "version": "0.1.0"
}
```

### Authentication

**Login**
```http
POST /auth/login
Content-Type: application/json

{
  "user_id": "vrushh_98",
  "password": "Vrush@nk09",
  "remember_me": true
}
```

Response:
```json
{
  "token": "...",
  "user_id": "vrushh_98",
  "message": "Login successful"
}
```

For full API docs, visit: `http://localhost:8000/docs`

---

## Project Rules

### Code Quality
- ✅ Type safety (TypeScript, Python type hints)
- ✅ Linting (ESLint, Flake8)
- ✅ Formatting (Prettier, Black)
- ✅ Testing (Unit + Integration)
- ✅ Documentation (Inline comments for WHY, not WHAT)

### Architecture
- ✅ Local-first (all data stored locally)
- ✅ Modular (clear ownership boundaries)
- ✅ Type-safe (no `any`, no untyped functions)
- ✅ Testable (no hidden dependencies)
- ✅ Maintainable (clear naming, small functions)

### Security
- ✅ Local authentication (no cloud login in V1)
- ✅ Encrypted storage (for Phase 3+)
- ✅ Permission model (granular control)
- ✅ Audit logging (every action logged)
- ✅ No telemetry (privacy-first)

---

## Contributing

This is a personal project, but the following guidelines apply:

1. **Read First**: Study `README_FIRST.md`, `CLAUDE.md`, `PROJECT_CONTEXT.md`
2. **Architecture**: Follow folder structure and module boundaries
3. **Testing**: Every feature needs tests
4. **Documentation**: Update docs when adding features
5. **Phase Gates**: Don't skip phases or quality gates

---

## Documentation

**Critical Reading:**
- `README_FIRST.md` — Start here
- `CLAUDE.md` — Operating instructions
- `PROJECT_CONTEXT.md` — Project overview
- `MASTER_BUILD_WORKFLOW.md` — Implementation order
- `PHASE_2_SCAFFOLD_COMPLETE.md` — Current status

**Detailed Specs:**
- `docs/` — 68+ specification documents
- `architecture/` — System design (26+ pages)
- `brand/` — Design system
- `prompts/` — Hirvi personality & prompt library
- `database/` — Database schema & strategy

---

## Known Issues

See `PHASE_2_SCAFFOLD_COMPLETE.md` for detailed limitations and planned fixes.

**Phase 2 Known Issues:**
- ⚠️ Hardcoded test credentials (fix in Phase 3)
- ⚠️ No real password hashing yet
- ⚠️ No JWT token management
- ⚠️ No database migrations system
- ⚠️ Backend requires running separately
- ⚠️ No AI integration yet

---

## Performance

### Targets
- ⚡ App startup: < 3 seconds
- ⚡ Dashboard render: < 500ms
- ⚡ Chat response: < 1 second
- 💾 Memory usage: < 500MB at idle
- 🎯 Scroll/interactions: 60 FPS (< 16ms latency)

### Achieved (Phase 2)
- ✅ Startup measured (scaffolding phase)
- ✅ Build optimized (Vite, code splitting)
- ✅ Assets optimized (icons, images)
- ⏳ E2E performance testing (Phase 3+)

---

## Deployment

### Development
```bash
npm run dev
```

### Production Build
```bash
npm run build
```

Creates:
- **Frontend**: `dist/` (optimized HTML/CSS/JS)
- **Desktop**: `src-tauri/target/release/` (Windows .exe, macOS .dmg, Linux AppImage)
- **Backend**: Python package ready for deployment

---

## Support & Feedback

For bugs, suggestions, or improvements:
1. Review existing issues in this repository
2. Check the documentation first
3. Open an issue with clear reproduction steps
4. Include your HEAVE version and OS

---

## License

**Private Project**. All rights reserved. This is Vrushh's personal operating system and is not intended for public distribution.

---

## Changelog

### v0.1.0 - Phase 2 (2026-07-05)
- ✨ Initial project scaffolding
- ✨ React + Tauri frontend setup
- ✨ FastAPI backend with SQLite
- ✨ Authentication shell (login page)
- ✨ Navigation shell (sidebar, topbar)
- ✨ Dashboard, Settings, Workspace shells
- ✨ Design system (dark mode, Liquid Glass)
- ✨ Development tooling configured
- 📚 68+ specification documents
- 📚 Comprehensive architecture documentation

---

## Vision

> "Think like software built by Apple. Fast. Beautiful. Minimal. Reliable. Private. Local-first. Intelligent."

HEAVE is not just an app—it's a personal operating system that anticipates your needs, respects your privacy, and makes you more productive.

---

**Built with ❤️ by Claude Code for Vrushh**

Next Phase: Phase 3 - Core Platform (Dashboard, Workspace, Memory, AI)
