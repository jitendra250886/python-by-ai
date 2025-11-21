# Platform Architecture Overview

This document describes the high-level architecture of the Python Master Course platform from backend to frontend and how it will be deployed.

## 1. Components

- **Backend API** (Django + Django REST Framework)
  - Location: `backend/`
  - Responsibilities:
    - User management and authentication
    - Course and lesson management
    - Enrollment and progress tracking (future)
    - Payments and subscriptions (future)
    - Project submissions and live classes (future)

- **Frontend Web App** (Next.js + React)
  - Location: `frontend/`
  - Responsibilities:
    - Landing/marketing pages
    - Course catalog and detail views
    - Student dashboard
    - Enrollment and payment UI
    - Lesson viewer and progress UI

- **Database**
  - Local/dev: SQLite (default Django configuration)
  - Production: PostgreSQL (recommended)

- **Static & Media Storage** (production)
  - Static assets (CSS, JS, images)
  - Uploaded files (project files, avatars, etc.)
  - Stored on disk or an object store (e.g., S3) depending on hosting

## 2. Data Flow

1. User visits the frontend (Next.js application).
2. Frontend calls backend API endpoints (e.g., `/api/courses/`, `/api/auth/me/`).
3. Backend reads/writes data in the database and returns JSON responses.
4. Frontend renders UI based on API responses.
5. For authenticated flows (login, enrollment, payments), frontend sends credentials/tokens to the backend, which communicates with the database and external providers (e.g., Stripe).

## 3. Environments

- **Development**
  - SQLite database
  - Django dev server on `http://localhost:8000/`
  - Next.js dev server on `http://localhost:3000/`

- **Production** (recommended MVP setup)
  - One Linux VPS (e.g., DigitalOcean droplet, AWS Lightsail, etc.)
  - PostgreSQL database (on the same server or managed DB service)
  - Django served via Gunicorn/Uvicorn behind Nginx
  - Next.js app served via `npm run start` (Node.js) or exported and served by Nginx
  - HTTPS enabled via Let's Encrypt

## 4. Deployment Strategy (MVP)

For the first version, the simplest robust approach is:

1. Provision a single VPS server.
2. Install system dependencies (Python, Node.js, PostgreSQL, Nginx).
3. Clone the `python-master-course` repo onto the server.
4. Create a Python virtual environment and install backend dependencies.
5. Install frontend dependencies and build the Next.js app.
6. Configure environment variables (database URL, secret key, debug flags, etc.).
7. Run database migrations and create an admin user.
8. Configure Gunicorn (or Uvicorn) + Nginx to serve the Django backend.
9. Configure Node.js (or Nginx static hosting) for the Next.js frontend.
10. Point your domain to the server and enable HTTPS.

The detailed, step-by-step commands for this flow are documented in `docs/deployment/END_TO_END_DEPLOYMENT.md`.
