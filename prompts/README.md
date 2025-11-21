# Prompts Directory

## Purpose
This directory contains summarized prompts and instructions used throughout the development of the Python Learning Platform. These prompts help track what has been requested from AI assistants and maintain consistency across development phases.

---

## Directory Structure

```
prompts/
├── README.md (this file)
├── phase-1-foundation/
├── phase-2-learning/
├── phase-3-projects/
├── phase-4-payments/
├── phase-5-live-classes/
├── phase-6-community/
├── phase-7-testing/
├── phase-8-launch/
└── templates/
```

---

## How to Use This Directory

### 1. Save Prompts After Each Major Task
When you request AI assistance for a specific feature or task, save a summarized version of:
- What you asked for
- Key requirements
- Important decisions made
- Code/files generated
- Next steps

### 2. Naming Convention
Use descriptive names with numbers for ordering:
```
01-feature-name.md
02-another-feature.md
```

### 3. Template Format
Each prompt file should follow this structure:

```markdown
# [Feature/Task Name]

## Date
YYYY-MM-DD

## Objective
Brief description of what you wanted to accomplish

## Prompt Summary
The essence of what was asked

## Key Requirements
- Requirement 1
- Requirement 2
- Requirement 3

## Output/Result
- What was created/generated
- Files modified
- Decisions made

## Next Steps
- What comes next
- Dependencies
- Follow-up tasks

## Notes
Any important context or considerations
```

---

## Phase Organization

### Phase 1: Foundation
**Timeline:** Months 1-2  
**Focus:** Core infrastructure, authentication, basic LMS

**Topics:**
- Backend setup (Django/FastAPI)
- Database schema design
- User authentication
- Frontend setup (React/Next.js)
- Basic course management
- Admin panel

### Phase 2: Learning Features
**Timeline:** Months 3-4  
**Focus:** Interactive learning tools

**Topics:**
- Code editor integration (Monaco)
- Code execution sandbox
- Quiz/exam system
- Progress tracking
- Video player integration
- Certificate generation

### Phase 3: Projects & Assessment
**Timeline:** Month 5  
**Focus:** Project submission and review

**Topics:**
- Project submission system
- File upload handling
- Code review dashboard
- Grading system
- Git integration
- Feedback mechanism

### Phase 4: Payment Integration
**Timeline:** Month 6  
**Focus:** Monetization

**Topics:**
- Stripe integration
- Subscription management
- Payment webhooks
- Invoice generation
- Access control
- Refund handling

### Phase 5: Live Classes
**Timeline:** Month 7  
**Focus:** Real-time learning

**Topics:**
- Class scheduling
- Calendar integration
- Zoom/Meet API integration
- Booking system
- Reminder automation
- Recording storage

### Phase 6: Community & Engagement
**Timeline:** Month 8  
**Focus:** Building community

**Topics:**
- Discussion forums
- Q&A system
- Real-time chat (WebSockets)
- Notification system
- Gamification
- Social features

### Phase 7: Testing & Optimization
**Timeline:** Month 9  
**Focus:** Quality assurance

**Topics:**
- Unit testing (backend)
- Component testing (frontend)
- Integration testing
- E2E testing
- Performance optimization
- Security audit

### Phase 8: Launch & Marketing
**Timeline:** Month 10  
**Focus:** Going live

**Topics:**
- Production deployment
- Marketing website
- SEO optimization
- Email campaigns
- Analytics setup
- Monitoring alerts

---

## Example Prompt Files

### Example 1: Backend Setup
**File:** `phase-1-foundation/01-backend-setup.md`

```markdown
# Django Backend Setup

## Date
2025-11-20

## Objective
Set up Django backend with project structure, settings, and initial configuration

## Prompt Summary
"Create a Django project for the Python learning platform with modular app structure, 
environment-based settings, and REST API configuration"

## Key Requirements
- Django 4.2+ with Django REST Framework
- Modular app architecture (users, courses, enrollments, etc.)
- Environment-based settings (dev, staging, prod)
- PostgreSQL database configuration
- JWT authentication setup
- CORS configuration

## Output/Result
- Created backend/ directory structure
- Set up Django project with config/
- Created apps/ directory with initial apps
- Configured settings in settings/base.py, development.py, production.py
- Added requirements/base.txt with dependencies
- Created Dockerfile and docker-compose.yml

## Next Steps
- Define database models
- Create API endpoints
- Set up user authentication
- Write initial tests

## Notes
- Used Django 4.2 for stability
- Chose PostgreSQL over MySQL for better JSON support
- JWT tokens expire in 24 hours (configurable)
```

### Example 2: Code Editor Integration
**File:** `phase-2-learning/01-code-editor.md`

```markdown
# Monaco Code Editor Integration

## Date
2025-11-25

## Objective
Integrate Monaco Editor (VS Code editor) into the frontend for in-browser code editing

## Prompt Summary
"Add Monaco Editor to React frontend with Python syntax highlighting, 
theme support, and code execution capability"

## Key Requirements
- Monaco Editor npm package
- Python syntax highlighting
- Dark/light theme support
- Code execution button
- Output panel
- Save code functionality
- Responsive design

## Output/Result
- Created components/editor/CodeEditor.jsx
- Created components/editor/CodeRunner.jsx
- Created components/editor/OutputPanel.jsx
- Added Monaco Editor configuration
- Connected to code execution API
- Styled with Tailwind CSS

## Next Steps
- Add code execution sandbox backend
- Implement test case runner
- Add code sharing feature
- Add keyboard shortcuts

## Notes
- Monaco Editor is 2MB+ (consider lazy loading)
- Supports 60+ languages (future expansion)
- Theme automatically syncs with app theme
```

---

## Benefits of Using This System

1. **Track Progress:** Easily see what has been built and what's pending
2. **Maintain Context:** Remember why certain decisions were made
3. **Onboard Team Members:** New developers can understand the project history
4. **Debugging:** Reference original requirements when fixing issues
5. **Documentation:** Serves as supplementary documentation
6. **AI Consistency:** Provide past prompts as context for future AI requests

---

## Best Practices

### Do's
✅ Summarize prompts concisely (1-2 pages max)  
✅ Include key decisions and trade-offs  
✅ Note any deviations from original plan  
✅ Update when requirements change  
✅ Reference related prompts  
✅ Include file paths and code structure

### Don'ts
❌ Don't copy entire codebases  
❌ Don't include sensitive information (API keys, passwords)  
❌ Don't duplicate information already in docs/  
❌ Don't save every small change  
❌ Don't make it too detailed (focus on high-level)

---

## Integration with Main Documentation

### Relationship to docs/ folder
- **docs/**: Formal, structured documentation (architecture, API, database)
- **prompts/**: Chronological record of development process and AI interactions

### When to Use Each
- Use **docs/** for: Architecture decisions, API reference, setup guides
- Use **prompts/** for: Development history, AI requests, feature implementation notes

---

## Quick Start

1. Create a new phase folder if it doesn't exist:
   ```powershell
   mkdir prompts\phase-X-name
   ```

2. Create a new prompt file:
   ```powershell
   New-Item -Path "prompts\phase-1-foundation\01-feature.md" -ItemType File
   ```

3. Copy the template (from templates/feature-template.md)

4. Fill in the details

5. Commit to git

---

## Templates

See `templates/` folder for:
- `feature-template.md` - Template for new features
- `bug-fix-template.md` - Template for bug fixes
- `refactor-template.md` - Template for code refactoring

---

**Last Updated:** 2025-11-20  
**Version:** 1.0
