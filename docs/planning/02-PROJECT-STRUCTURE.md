# Project Structure Documentation

## Overview
This document details the complete folder structure for the Python Learning Platform project, explaining the purpose of each directory and key files.

---

## Root Directory Structure

```
python-master-course/
├── backend/                    # Django/FastAPI application
├── frontend/                   # React/Next.js application
├── code-executor/             # Code execution microservice
├── docs/                      # All documentation
├── prompts/                   # AI development prompts
├── scripts/                   # Utility scripts
├── 01-beginner/               # Course content (Level 1)
├── 02-intermediate/           # Course content (Level 2)
├── 03-advanced/               # Course content (Level 3)
├── 04-libraries/              # Course content (Level 4)
├── 05-applications/           # Course content (Level 5)
├── 06-projects/               # Course content (Level 6)
├── examples/                  # Code examples
├── resources/                 # Additional resources
├── docker-compose.yml         # Docker orchestration
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # Project overview
└── WARP.md                    # Warp AI guidance
```

---

## Backend Structure (Django/FastAPI)

```
backend/
├── config/                    # Project configuration
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py           # Base settings
│   │   ├── development.py    # Dev environment
│   │   ├── production.py     # Prod environment
│   │   └── test.py           # Test environment
│   ├── urls.py               # URL routing
│   ├── asgi.py               # ASGI config
│   └── wsgi.py               # WSGI config
│
├── apps/                      # Django apps
│   ├── users/                # User management
│   │   ├── models.py         # User, Profile models
│   │   ├── serializers.py    # DRF serializers
│   │   ├── views.py          # API views
│   │   ├── urls.py           # User routes
│   │   ├── permissions.py    # Custom permissions
│   │   ├── signals.py        # Signal handlers
│   │   └── tests/
│   │
│   ├── courses/              # Course management
│   │   ├── models.py         # Course, Lesson, Module
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py          # Django admin config
│   │   └── tests/
│   │
│   ├── enrollments/          # Course enrollments
│   │   ├── models.py         # Enrollment, Progress
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── tests/
│   │
│   ├── assessments/          # Quizzes & Exams
│   │   ├── models.py         # Quiz, Question, Answer
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── grading.py        # Auto-grading logic
│   │   └── tests/
│   │
│   ├── projects/             # Project submissions
│   │   ├── models.py         # Project, Submission
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── validators.py     # Code validation
│   │   └── tests/
│   │
│   ├── payments/             # Payment processing
│   │   ├── models.py         # Payment, Subscription
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── stripe_handler.py # Stripe integration
│   │   ├── webhooks.py       # Payment webhooks
│   │   └── tests/
│   │
│   ├── live_classes/         # Live class management
│   │   ├── models.py         # LiveClass, Booking
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── zoom_api.py       # Zoom integration
│   │   └── tests/
│   │
│   ├── notifications/        # Notification system
│   │   ├── models.py         # Notification
│   │   ├── email_service.py  # Email sending
│   │   ├── sms_service.py    # SMS sending
│   │   ├── push_service.py   # Push notifications
│   │   └── tests/
│   │
│   ├── forums/               # Discussion forums
│   │   ├── models.py         # Thread, Post, Reply
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── tests/
│   │
│   ├── analytics/            # Analytics & reporting
│   │   ├── models.py         # UserActivity, CourseStats
│   │   ├── views.py
│   │   ├── reports.py        # Report generation
│   │   └── tests/
│   │
│   └── certificates/         # Certificate generation
│       ├── models.py         # Certificate
│       ├── generator.py      # PDF generation
│       └── tests/
│
├── core/                      # Core utilities
│   ├── authentication.py     # JWT auth
│   ├── permissions.py        # Base permissions
│   ├── pagination.py         # Custom pagination
│   ├── exceptions.py         # Custom exceptions
│   └── mixins.py             # View mixins
│
├── media/                     # User-uploaded files
│   ├── avatars/
│   ├── course_images/
│   ├── videos/
│   └── submissions/
│
├── static/                    # Static files
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/                 # Email templates
│   ├── emails/
│   └── certificates/
│
├── tests/                     # Integration tests
│   ├── conftest.py           # Pytest fixtures
│   ├── test_api.py
│   └── test_integration.py
│
├── manage.py                  # Django management
├── requirements/              # Dependencies
│   ├── base.txt              # Base requirements
│   ├── development.txt       # Dev dependencies
│   ├── production.txt        # Prod dependencies
│   └── test.txt              # Test dependencies
│
├── Dockerfile                 # Docker image
├── .env.example              # Environment template
└── pytest.ini                # Pytest configuration
```

---

## Frontend Structure (React/Next.js)

```
frontend/
├── public/                    # Static assets
│   ├── images/
│   ├── icons/
│   ├── favicon.ico
│   └── robots.txt
│
├── src/
│   ├── components/           # Reusable components
│   │   ├── common/
│   │   │   ├── Button.jsx
│   │   │   ├── Input.jsx
│   │   │   ├── Modal.jsx
│   │   │   ├── Loader.jsx
│   │   │   └── Alert.jsx
│   │   │
│   │   ├── layout/
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   └── Navigation.jsx
│   │   │
│   │   ├── course/
│   │   │   ├── CourseCard.jsx
│   │   │   ├── CourseList.jsx
│   │   │   ├── LessonPlayer.jsx
│   │   │   ├── VideoPlayer.jsx
│   │   │   └── ProgressBar.jsx
│   │   │
│   │   ├── editor/
│   │   │   ├── CodeEditor.jsx    # Monaco editor
│   │   │   ├── CodeRunner.jsx
│   │   │   └── OutputPanel.jsx
│   │   │
│   │   ├── quiz/
│   │   │   ├── QuizCard.jsx
│   │   │   ├── Question.jsx
│   │   │   └── Results.jsx
│   │   │
│   │   ├── project/
│   │   │   ├── ProjectCard.jsx
│   │   │   ├── SubmissionForm.jsx
│   │   │   └── ReviewPanel.jsx
│   │   │
│   │   └── dashboard/
│   │       ├── StatsCard.jsx
│   │       ├── ProgressChart.jsx
│   │       └── ActivityFeed.jsx
│   │
│   ├── pages/                # Page components
│   │   ├── index.jsx         # Home page
│   │   ├── login.jsx
│   │   ├── register.jsx
│   │   ├── courses/
│   │   │   ├── index.jsx     # Course listing
│   │   │   └── [id].jsx      # Course detail
│   │   ├── learn/
│   │   │   └── [courseId]/
│   │   │       └── [lessonId].jsx
│   │   ├── dashboard/
│   │   │   ├── index.jsx
│   │   │   ├── courses.jsx
│   │   │   ├── projects.jsx
│   │   │   └── settings.jsx
│   │   ├── admin/
│   │   │   ├── index.jsx
│   │   │   ├── courses.jsx
│   │   │   ├── users.jsx
│   │   │   └── analytics.jsx
│   │   └── _app.jsx          # App wrapper
│   │
│   ├── services/             # API services
│   │   ├── api.js            # Axios instance
│   │   ├── authService.js
│   │   ├── courseService.js
│   │   ├── userService.js
│   │   ├── paymentService.js
│   │   └── projectService.js
│   │
│   ├── store/                # State management
│   │   ├── index.js          # Store configuration
│   │   ├── slices/
│   │   │   ├── authSlice.js
│   │   │   ├── courseSlice.js
│   │   │   ├── userSlice.js
│   │   │   └── uiSlice.js
│   │   └── hooks.js          # Custom hooks
│   │
│   ├── hooks/                # Custom React hooks
│   │   ├── useAuth.js
│   │   ├── useCourse.js
│   │   ├── useDebounce.js
│   │   └── useLocalStorage.js
│   │
│   ├── utils/                # Utility functions
│   │   ├── formatters.js     # Date, currency formatting
│   │   ├── validators.js     # Form validation
│   │   ├── constants.js      # App constants
│   │   └── helpers.js        # Helper functions
│   │
│   ├── styles/               # Styling
│   │   ├── globals.css       # Global styles
│   │   ├── variables.css     # CSS variables
│   │   └── themes/
│   │       ├── light.css
│   │       └── dark.css
│   │
│   └── config/               # Configuration
│       ├── env.js            # Environment variables
│       └── routes.js         # Route definitions
│
├── tests/                    # Frontend tests
│   ├── components/
│   ├── pages/
│   └── utils/
│
├── package.json              # Dependencies
├── package-lock.json
├── next.config.js            # Next.js config
├── tailwind.config.js        # Tailwind CSS config
├── tsconfig.json             # TypeScript config (if used)
├── .eslintrc.js              # ESLint rules
├── .prettierrc               # Prettier config
├── jest.config.js            # Jest config
└── Dockerfile                # Docker image
```

---

## Code Executor Microservice

```
code-executor/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app
│   ├── executor.py           # Code execution logic
│   ├── sandbox.py            # Docker sandbox
│   ├── validators.py         # Code validation
│   └── models.py             # Pydantic models
│
├── tests/
│   ├── test_executor.py
│   └── test_sandbox.py
│
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## Documentation Structure

```
docs/
├── planning/                 # Project planning
│   ├── 01-HIGH-LEVEL-PLAN.md
│   ├── 02-PROJECT-STRUCTURE.md (this file)
│   ├── 03-WORKFLOW.md
│   ├── 04-TIMELINE.md
│   └── 05-MILESTONES.md
│
├── architecture/             # System architecture
│   ├── 01-OVERVIEW.md
│   ├── 02-BACKEND-ARCHITECTURE.md
│   ├── 03-FRONTEND-ARCHITECTURE.md
│   ├── 04-DATABASE-DESIGN.md
│   ├── 05-API-DESIGN.md
│   ├── 06-SECURITY.md
│   └── diagrams/
│       ├── system-architecture.png
│       ├── database-erd.png
│       └── user-flows.png
│
├── api/                      # API documentation
│   ├── 01-AUTHENTICATION.md
│   ├── 02-USERS.md
│   ├── 03-COURSES.md
│   ├── 04-ENROLLMENTS.md
│   ├── 05-ASSESSMENTS.md
│   ├── 06-PROJECTS.md
│   ├── 07-PAYMENTS.md
│   └── 08-LIVE-CLASSES.md
│
├── database/                 # Database documentation
│   ├── 01-SCHEMA.md
│   ├── 02-MIGRATIONS.md
│   ├── 03-INDEXES.md
│   └── schema.sql
│
├── deployment/               # Deployment guides
│   ├── 01-LOCAL-SETUP.md
│   ├── 02-DOCKER-SETUP.md
│   ├── 03-AWS-DEPLOYMENT.md
│   ├── 04-CI-CD.md
│   └── 05-MONITORING.md
│
├── frontend/                 # Frontend documentation
│   ├── 01-SETUP.md
│   ├── 02-COMPONENTS.md
│   ├── 03-STATE-MANAGEMENT.md
│   └── 04-STYLING.md
│
├── backend/                  # Backend documentation
│   ├── 01-SETUP.md
│   ├── 02-MODELS.md
│   ├── 03-APIS.md
│   └── 04-TESTING.md
│
└── design/                   # UI/UX designs
    ├── wireframes/
    ├── mockups/
    └── style-guide.md
```

---

## Prompts Structure

```
prompts/
├── README.md                 # How to use prompts
│
├── phase-1-foundation/
│   ├── 01-backend-setup.md
│   ├── 02-database-models.md
│   ├── 03-auth-system.md
│   └── 04-frontend-setup.md
│
├── phase-2-learning/
│   ├── 01-code-editor.md
│   ├── 02-quiz-system.md
│   └── 03-progress-tracking.md
│
├── phase-3-projects/
│   ├── 01-submission-system.md
│   └── 02-review-system.md
│
├── phase-4-payments/
│   ├── 01-stripe-integration.md
│   └── 02-subscription-logic.md
│
├── phase-5-live-classes/
│   ├── 01-scheduling.md
│   └── 02-zoom-integration.md
│
├── phase-6-community/
│   ├── 01-forums.md
│   └── 02-notifications.md
│
└── templates/
    ├── feature-template.md
    └── bug-fix-template.md
```

---

## Scripts Directory

```
scripts/
├── setup/
│   ├── setup_dev.sh          # Development setup
│   ├── setup_db.sh           # Database setup
│   └── install_deps.sh       # Install dependencies
│
├── database/
│   ├── seed_data.py          # Seed database
│   ├── backup.sh             # Backup script
│   └── migrate.sh            # Run migrations
│
├── deployment/
│   ├── deploy_staging.sh
│   ├── deploy_production.sh
│   └── rollback.sh
│
└── utils/
    ├── generate_secrets.py   # Generate secret keys
    └── cleanup.py            # Cleanup old data
```

---

## Course Content Structure (Existing)

```
01-beginner/
02-intermediate/
03-advanced/
04-libraries/
05-applications/
06-projects/
examples/
resources/
```

These directories remain as-is for course content. The platform will serve this content through the web interface.

---

## Key Configuration Files

### docker-compose.yml
Orchestrates all services (backend, frontend, database, redis, code-executor)

### .env.example
Template for environment variables:
- Database credentials
- API keys (Stripe, Zoom, SendGrid)
- JWT secrets
- AWS credentials
- Third-party service URLs

### .gitignore
Excludes:
- `venv/`, `node_modules/`
- `.env`, secrets
- `*.pyc`, `__pycache__/`
- `media/`, user uploads
- Build artifacts

---

## Notes

1. **Modular Design:** Each app/component is self-contained
2. **Separation of Concerns:** Clear boundaries between frontend, backend, services
3. **Scalability:** Microservices architecture allows independent scaling
4. **Maintainability:** Organized structure makes code easy to find and maintain
5. **Testing:** Dedicated test directories for all components

---

**Last Updated:** 2025-11-20  
**Version:** 1.0
