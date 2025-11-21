# Deployment Guide

This guide explains how to prepare course content for the web and where to find the **full end-to-end deployment instructions** for the platform.

## 1. Converting Notebooks to Web-Ready Content

To convert a single notebook to Markdown:

```bash
jupyter nbconvert --to markdown 01-beginner/01_introduction_to_python.ipynb
```

You can repeat this for other notebooks or automate it using the scripts in `project_scripts/`.

## 2. Full Platform Deployment

For a complete, step-by-step guide that covers:

- How to choose and purchase hosting
- How to set up a Linux server
- How to deploy the **Django backend** (`backend/`)
- How to deploy the **Next.js frontend** (`frontend/`)
- How to configure Nginx, domains, and HTTPS
- A final launch checklist

see:

- `docs/architecture/PLATFORM_OVERVIEW.md` – architecture and components
- `docs/backend/README.md` – backend (Django + DRF) setup and libraries
- `docs/frontend/README.md` – frontend (Next.js) setup
- `docs/deployment/END_TO_END_DEPLOYMENT.md` – end-to-end server + hosting + launch guide
