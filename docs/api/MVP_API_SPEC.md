# MVP API Specification

This document defines the **minimum API surface** required for the first revenue-generating release of the Python Master Course platform.

It focuses on:

1. Authentication and user profile
2. Course catalog and lessons
3. Enrollment
4. Orders and payments

Implementation initially uses Django + Django REST Framework.

---

## 1. Authentication & User Profile

> Note: For MVP, you can start with session-based auth via Django's built-in login views or add a simple JSON-based login endpoint. This spec describes JSON-style endpoints.

### 1.1 Register

- **POST** `/api/auth/register/`
- **Body (JSON):**
  - `username` (string)
  - `email` (string)
  - `password` (string)
- **Response 201 (JSON):**
  - `id`, `username`, `email`, `role`

### 1.2 Login

- **POST** `/api/auth/login/`
- **Body (JSON):**
  - `username` or `email`
  - `password`
- **Response 200 (JSON):**
  - `user`: `{ id, username, email, role }`
  - `session` or `token`: implementation-dependent (session cookie or JWT)

### 1.3 Logout

- **POST** `/api/auth/logout/`
- **Behavior:**
  - Invalidates current session or token.

### 1.4 Current User

- **GET** `/api/auth/me/`
- **Auth:** required
- **Response 200 (JSON):**
  - `id`, `username`, `email`, `first_name`, `last_name`, `role`

---

## 2. Courses & Lessons

Public endpoints for the catalog plus authenticated access for full content.

### 2.1 List Courses

- **GET** `/api/courses/`
- **Query Params (optional):**
  - `search` – text search on title/description
- **Response 200 (JSON):**
  - `results`: list of courses
    - `id`, `title`, `slug`, `short_description`, `is_published`

### 2.2 Course Detail

- **GET** `/api/courses/{id}/`
- **Response 200 (JSON):**
  - `id`, `title`, `slug`, `short_description`, `full_description`, `is_published`
  - `lessons`: list of lessons with:
    - `id`, `title`, `order`, `is_preview`

### 2.3 Lesson Detail (with Access Control)

- **GET** `/api/lessons/{id}/`
- **Behavior:**
  - If `lesson.is_preview == true`, return content without enrollment.
  - Otherwise, require an active `Enrollment` for the associated `Course`.
- **Response 200 (JSON):**
  - `id`, `course_id`, `title`, `order`
  - `content` (HTML or Markdown rendered)

> Implementation detail: the `content` field may be derived from `content_path` in the `Lesson` model by loading the appropriate file.

---

## 3. Enrollment

### 3.1 List My Enrollments

- **GET** `/api/enrollments/`
- **Auth:** required (student)
- **Response 200 (JSON):**
  - List of:
    - `id`
    - `course`: `{ id, title, slug }`
    - `status`
    - `started_at`, `expires_at`
    - `progress_percent` (optional, derived)

### 3.2 Enrollment Detail

- **GET** `/api/enrollments/{id}/`
- **Auth:** required
- **Response 200 (JSON):**
  - Basic enrollment fields plus:
  - `lessons`: list with `id`, `title`, `order`, `is_completed`

### 3.3 Lesson Progress Update

- **POST** `/api/enrollments/{enrollment_id}/lessons/{lesson_id}/progress/`
- **Auth:** required (must own the enrollment)
- **Body (JSON):**
  - `is_completed` (boolean)
- **Response 200 (JSON):**
  - Updated status for that lesson (including `completed_at`)

This minimal set of endpoints is enough to track and display a student's progress through a course.

---

## 4. Orders & Payments (Stripe-Oriented MVP)

The MVP integrates with a payment provider like Stripe, but keeps the platform logic simple.

### 4.1 Create Checkout Session for a Course

- **POST** `/api/orders/create-checkout-session/`
- **Auth:** required
- **Body (JSON):**
  - `course_id` (integer)
- **Behavior:**
  - Validates that the course exists and is purchasable.
  - Creates an `Order` with `status="pending"`.
  - Creates a checkout session with the payment provider.
- **Response 200 (JSON):**
  - `checkout_url` – URL to redirect the user to complete payment.
  - `order_id`

### 4.2 Payment Webhook (from Provider)

- **POST** `/api/orders/webhook/`
- **Auth:** no (secured with provider secret)
- **Behavior:**
  - Validates webhook signature.
  - Finds the `Order` by `provider_session_id` or `provider_payment_id`.
  - If payment is successful:
    - Marks the `Order` as `paid`.
    - Creates an `Enrollment` for the user → course if not already existing.
  - If payment fails:
    - Marks the `Order` as `failed`.

- **Response 200/204:**
  - Acknowledges receipt; no user-facing response.

### 4.3 List My Orders (Optional)

- **GET** `/api/orders/`
- **Auth:** required
- **Response 200 (JSON):**
  - List of orders for the current user with:
    - `id`, `course`, `amount`, `currency`, `status`, `created_at`

---

## 5. Admin / Instructor APIs (Later)

For the MVP, admins and instructors can use the **Django admin** to:

- Create and edit courses and lessons
- Manage users and enrollments
- View orders

Later, you can add dedicated admin APIs under `/api/admin/...` with proper permissions.

---

## 6. Summary of MVP Endpoints

**Public / semi-public:**

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/logout/`
- `GET  /api/courses/`
- `GET  /api/courses/{id}/`
- `GET  /api/lessons/{id}/` (with preview/enrollment logic)

**Authenticated (student):**

- `GET  /api/auth/me/`
- `GET  /api/enrollments/`
- `GET  /api/enrollments/{id}/`
- `POST /api/enrollments/{enrollment_id}/lessons/{lesson_id}/progress/`
- `POST /api/orders/create-checkout-session/`
- `GET  /api/orders/` (optional)

**System / provider:**

- `POST /api/orders/webhook/` (Stripe or other provider)

This API surface is intentionally small but supports the core flows of the platform:

- Users can sign up, log in, and see their profile.
- Visitors can browse courses and preview lessons.
- Students can pay for a course and get enrolled.
- Students can track their progress.
- The platform records orders and enrollment state for business and support.
