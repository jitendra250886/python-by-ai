# Backend (Django + Django REST Framework)

This document explains how the backend of the Python Master Course platform is structured, which libraries it uses, and how to run it from scratch.

## 1. Overview

The backend is a **Django** project with a **Django REST Framework (DRF)** API.

- Project root: `backend/`
- Django project: `backend/core/`
- Apps:
  - `backend/accounts/` – custom `User` model and authentication-related logic
  - `backend/courses/` – `Course` and `Lesson` models and read-only course API

### Key Libraries

- **Django** – full-featured web framework (ORM, admin, auth, migrations, etc.)
- **Django REST Framework (DRF)** – tools for building REST APIs (serializers, viewsets, routers)

These are installed via:

```bash
pip install "django>=5,<6" djangorestframework
```

## 2. Settings

Main settings file: `backend/core/settings.py`.

Important configuration:

- `INSTALLED_APPS` includes:
  - `rest_framework` – DRF
  - `accounts`, `courses` – local apps
- `AUTH_USER_MODEL = 'accounts.User'` – tells Django to use the custom `User` model.
- `REST_FRAMEWORK` – basic DRF configuration (authentication & permissions).

SQLite is used by default for local development (file `backend/db.sqlite3`).

## 3. Models

### 3.1 User (accounts.User)

File: `backend/accounts/models.py`.

The platform uses a **custom user model** that extends `AbstractUser` and adds a `role` field:

- `username`, `email`, `password`, etc. – from Django `AbstractUser`
- `role` – one of:
  - `student`
  - `instructor`
  - `admin`

Having a custom user model early avoids painful migrations later when adding platform-specific fields.

### 3.2 Course, Lesson, Enrollment, Progress, Orders (courses)

File: `backend/courses/models.py`.

- `Course`
  - `title`, `slug`, `short_description`, `full_description`
  - `price` – decimal price used when creating orders
  - `is_published` – whether course is visible in the public API
  - `created_at`, `updated_at`

- `Lesson`
  - `course` – FK to `Course` (with `related_name="lessons"`)
  - `title`
  - `order` – lesson position within the course
  - `content_path` – relative path to rendered lesson content (e.g. generated HTML/Markdown)
  - `is_preview` – if `True`, lesson can be shown without enrollment
  - `created_at`, `updated_at`

- `Enrollment`
  - Links `user` ↔ `course`
  - Fields: `status` (active/cancelled/expired), `source` (purchase/manual/admin_grant),
    `started_at`, `expires_at`, timestamps

- `LessonProgress`
  - Links `enrollment` ↔ `lesson`
  - Tracks `is_completed`, `completed_at`, `last_viewed_at`

- `Order`
  - Records payments: `user`, `course`, `amount`, `currency`, `status` (pending/paid/failed/refunded)
  - Stripe metadata: `provider`, `provider_session_id`, `provider_payment_id`

These models together support selling access to courses, tracking enrollment and lesson completion, and recording payment state.

## 4. API Endpoints

Routing file: `backend/core/urls.py`.

### 4.1 Auth APIs

- `POST /api/auth/register/` – register a new user
- `POST /api/auth/login/` – log in (session-based)
- `POST /api/auth/logout/` – log out current user
- `GET  /api/auth/me/` – current authenticated user profile

### 4.2 Course & Lesson APIs

Using DRF `DefaultRouter` and viewsets:

- `GET /api/courses/` – list all **published** courses
- `GET /api/courses/{id}/` – details for a single course (including its lessons)
- `GET /api/lessons/` – list lessons
- `GET /api/lessons/{id}/` – lesson detail
  - If `is_preview=True`, public
  - Otherwise requires an active `Enrollment` for the course

Implemented in:

- Viewsets: `backend/courses/views.py`
- Serializers: `backend/courses/serializers.py`

### 4.3 Enrollment & Progress APIs

- `GET /api/enrollments/` – list enrollments for current user (with `progress_percent`)
- `GET /api/enrollments/{id}/` – enrollment detail + per-lesson completion flags
- `POST /api/enrollments/{enrollment_id}/lessons/{lesson_id}/progress/` – update lesson completion

### 4.4 Orders & Payments (Stripe)

- `GET  /api/orders/` – list orders for current user
- `POST /api/orders/create-checkout-session/` – create Stripe Checkout Session for a course
  - Creates `Order(status="pending")`
  - Returns `checkout_url` (Stripe-hosted payment page)
- `POST /api/orders/webhook/` – Stripe webhook endpoint
  - Verifies signature using `STRIPE_WEBHOOK_SECRET`
  - On `checkout.session.completed`, marks `Order` as `paid` and creates `Enrollment`

## 5. Running the Backend Locally

### 5.1 Install Dependencies

From the project root:

```bash
pip install "django>=5,<6" djangorestframework
```

If you prefer, you can create and activate a virtual environment first.

### 5.2 Apply Migrations

```bash
python backend/manage.py migrate
```

This creates the database tables for Django auth, sessions, admin, and the `accounts` and `courses` apps.

### 5.3 Create a Superuser

```bash
python backend/manage.py createsuperuser
```

Follow the prompts to create an admin account. You will use this to log into the Django admin panel.

### 5.4 Run the Development Server

```bash
python backend/manage.py runserver 0.0.0.0:8000
```

Then open `http://localhost:8000/admin/` to access the admin and `http://localhost:8000/api/courses/` to see the API.

## 6. Next Steps

Later iterations will extend the backend with:

- Authentication endpoints (login, logout, registration, JWT)
- Enrollment and progress tracking models
- Payment integration (Stripe)
- Project submissions and live classes

As those features are added, this document can be extended with new models and endpoints.
