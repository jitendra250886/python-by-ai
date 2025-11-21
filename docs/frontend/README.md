# Frontend (Next.js + React)

This document explains how the frontend for the Python Master Course platform is structured and how it interacts with the Django backend.

The frontend has been scaffolded as a **Next.js (React)** application in the `frontend/` directory.

## 1. Overview

The frontend is a **Next.js (React)** application in the `frontend/` directory.

- Framework: **Next.js** (React-based, supports server-side rendering and static generation)
- Language: **TypeScript** (recommended)
- UI: any modern UI library (e.g., Tailwind CSS or Material UI)
- API Access: communicates with the Django/DRF backend via HTTP calls to `/api/...` endpoints.

## 2. Planned Directory Structure

The generated structure (App Router + Tailwind) includes:

- `frontend/`
  - `app/` – route definitions
  - `app/lib/` – API client helpers
  - `public/` – static assets

Currently implemented core routes:

- `/` – simple landing page with links to Login and Courses
- `/login` – login form that calls `POST /api/auth/login/`
- `/courses` – list of courses (calls `GET /api/courses/` and can initiate checkout)

More routes (course detail, dashboard, etc.) can be added on top of this foundation.

## 3. Creating the Frontend App

From the project root (one level above `frontend/`):

```bash
npx create-next-app@latest frontend --typescript
```

Follow the prompts (you can accept defaults). This creates the `frontend/` directory with a working Next.js app.

## 4. Running the Frontend Locally

From the `frontend/` directory:

```bash
cd frontend
npm install
npm run dev
```

Then open `http://localhost:3000/` in your browser.

## 5. Connecting to the Backend

The frontend will call the Django API (running on `http://localhost:8000/` during development).

Examples:

- Fetch courses:
  - `GET http://localhost:8000/api/courses/`
- Fetch course details:
  - `GET http://localhost:8000/api/courses/{id}/`
- Fetch current user profile:
  - `GET http://localhost:8000/api/auth/me/` (after login is implemented)

In Next.js, you can call these endpoints using `fetch` or a library like `axios`.

## 6. Production Build

Before deployment, build the production frontend bundle:

```bash
cd frontend
npm run build
npm run start
```

The `npm run build` command produces an optimized build that can be served by Node.js or exported and served as static assets (depending on the configuration).

As the frontend is implemented, this document can be expanded with:

- Auth flow (login, logout, protected routes)
- Course enrollment UI
- Payment pages
- Dashboard views and progress tracking.
