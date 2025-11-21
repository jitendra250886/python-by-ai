# MVP Data Model

This document describes the **minimal data model** needed for the first revenue-generating version (MVP) of the Python Master Course platform.

It builds on the existing models:

- `accounts.User` – custom user with `role`
- `courses.Course` and `courses.Lesson`

and adds enrollment and payment-related entities.

---

## 1. Core Entities

### 1.1 User (accounts.User)

Already implemented as a custom user model with a `role` field:

- `username`, `email`, `password`, `first_name`, `last_name`
- `role` ∈ {`student`, `instructor`, `admin`}

In the MVP:

- Students purchase access to **courses** or to a **site-wide subscription** (future extension).
- Instructors/admins use the admin interface to manage content and users.

### 1.2 Course (courses.Course)

Already implemented with basic fields:

- `title`, `slug`, `short_description`, `full_description`
- `is_published`
- `created_at`, `updated_at`

Courses are the primary item a student purchases/enrolls into in the MVP.

### 1.3 Lesson (courses.Lesson)

Represents a single piece of content inside a course:

- `course` (FK → Course, `related_name="lessons"`)
- `title`
- `order`
- `content_path` (path to rendered Markdown/HTML)
- `is_preview` (public preview or not)
- `created_at`, `updated_at`

---

## 2. Enrollment & Progress

### 2.1 Enrollment

**Entity:** `Enrollment`

Represents a student's access to a course.

Suggested fields:

- `id`
- `user` (FK → User)
- `course` (FK → Course)
- `status` – e.g. `active`, `cancelled`, `expired`
- `source` – e.g. `purchase`, `manual`, `admin_grant`
- `started_at` – when the user first accessed the course
- `expires_at` – optional expiry date (for subscriptions or time-limited offers)
- `created_at`, `updated_at`

**Relationships:**

- Many-to-many between `User` and `Course` via `Enrollment`.

### 2.2 Lesson Progress

**Entity:** `LessonProgress`

Tracks whether a user has completed a lesson inside an enrolled course.

Fields:

- `id`
- `enrollment` (FK → Enrollment)
- `lesson` (FK → Lesson)
- `is_completed` – boolean
- `completed_at` – timestamp (nullable)
- `last_viewed_at` – timestamp (nullable)

This enables:

- Per-lesson completion
- Overall course progress percentage (completed lessons / total lessons)

---

## 3. Payments & Orders

The MVP only needs **basic payment tracking**. The actual payment processing will be handled by a provider like Stripe, but we still need internal records.

### 3.1 Product Types

For the first version we support:

- **Course purchase** – one-time purchase of a single course
- (Future) **Subscription** – site-wide access

In the data model, we can keep it simple and tie payments directly to courses via an `Order` model.

### 3.2 Order

**Entity:** `Order`

Represents a payment attempt/transaction.

Fields:

- `id`
- `user` (FK → User)
- `course` (FK → Course, nullable if later we support multiple courses or subscriptions)
- `amount` – decimal
- `currency` – e.g. `USD`
- `status` – `pending`, `paid`, `failed`, `refunded`
- `provider` – e.g. `stripe`
- `provider_session_id` – checkout session or intent ID
- `provider_payment_id` – payment ID
- `created_at`
- `updated_at`

### 3.3 Payment → Enrollment Link

We need to connect successful payments to enrollments.

Options:

1. **Order creates Enrollment directly:**
   - After a successful payment (via webhook or redirect), we create an `Enrollment` for the user and course.
   - `Enrollment.source = "purchase"`.

2. **Order stores Enrollment reference:**
   - `Order` gets a nullable FK `enrollment` and is filled when the enrollment is created.

For the MVP, option 1 is enough: **Order → create Enrollment**, and we can always look up `Enrollment` by `(user, course)`.

---

## 4. Other Supporting Entities (Future)

These are not required for the first MVP, but are natural next steps and should be kept in mind when designing tables:

- `Subscription` – recurring billing, multiple courses
- `Invoice` – detailed billing records
- `DiscountCode` / `Coupon`
- `LiveClass`, `LiveClassSession`, `LiveClassEnrollment`
- `ProjectSubmission` – for hands-on projects with instructor feedback

The MVP schema is deliberately small to make implementation and deployment faster, while leaving room to grow.

---

## 5. Summary

For the MVP, the key new tables to implement in addition to existing models are:

- `Enrollment` – user ↔ course access
- `LessonProgress` – per-lesson completion tracking
- `Order` – records of payments and their status

These tables, combined with `User`, `Course`, and `Lesson`, are enough to:

- Sell access to individual courses
- Track which users are enrolled in which courses
- Track lesson completion and course progress
- Maintain a basic payment history for auditing and support.
