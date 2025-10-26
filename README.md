# Unified Intelligence Platform for Startup Incubation
# Alcubator

## Project Overview

The **Unified Intelligence Platform** is a data-driven ERP system designed to manage the entire lifecycle of startups in incubation ecosystems. It unifies fragmented tools into a single platform to streamline:

- Startup onboarding and milestone tracking
- Grant and fund management
- Facility and resource booking
- Mentor and investor engagement
- Analytics and reporting

The platform improves operational efficiency, supports data-driven decisions, and strengthens the startup ecosystem.

---

## Feature Comparison

| Feature Category | Old Implementation | New Implementation / Updates |
|-----------------|-----------------|------------------------------|
| **Startup Lifecycle Management** | Online applications, milestone tracking, alumni monitoring | Full dashboard for startups, admin can manage all startups, AI-assisted evaluation for pitch scoring |
| **Grant & Financial Management** | Grant tracking, disbursement workflows, compliance reporting | Dashboard for grants, CRUD operations, mentor & admin views, AI evaluation suggestions for funding |
| **Facility & Resource Booking** | Real-time booking, calendar integration, utilization analytics | Mobile-friendly booking UI, glassmorphism design, resource utilization tracking |
| **Mentor & Investor Management** | Profile directories, matching algorithms, interaction logging | Mentor dashboard with startup interaction tracking, CRUD operations, AI suggestions for mentor-startup matching |
| **Analytics & Reporting** | Dashboards for incubator managers and funding agencies | Enhanced dashboards with AI evaluation results, visual representation for admins and mentors |
| **Communication & Collaboration** | Notifications, messaging, email integration, audit trails | Same, plus improved UI/UX with polished, responsive frontend |
| **UI/UX Design** | Standard React.js UI | Fully responsive glassmorphism design, mobile support via React Native, improved usability |
| **Authentication & Security** | JWT, RBAC, TLS 1.3, AES-256 encryption | Same, plus role-based access for frontend dashboards, token storage for mobile |

---

## Additional Features Implemented

| Feature | Description |
|---------|-------------|
| AI Evaluation | Admin, mentor, and startup dashboards support pitch evaluation using AI with scoring and feedback. |
| Glassmorphism UI | Modern translucent, blurred card design across web and mobile. |
| Mobile Support | React Native app for Android/iOS supporting login, CRUD for startups, grants, mentors, and facilities. |
| Role-Based Dashboards | Admin, mentor, and startup dashboards with tailored views and access restrictions. |
| Enhanced Forms & UX | Responsive inputs, better buttons, validation, and error handling. |
| Dynamic Frontend | Data fetched from backend with proper token authentication and CRUD functionality for all resources. |

---

## Tech Stack

- **Backend**: FastAPI (Python)  
- **Database**: SQL 
- **Frontend**: HTML, React Native (Mobile)  
- **Async Tasks**: Celery + Redis/RabbitMQ  
- **Real-time Communication**: WebSockets  
- **Deployment**: Docker + Kubernetes (Cloud / On-Premise)  
- **Security**: JWT, RBAC, TLS 1.3, AES-256 encryption  

---

## Getting Started

### Prerequisites

- Python 3.11+  
- PostgreSQL 14+  
- Node.js 18+ (frontend)  
- Docker (optional, for containerized setup)  

### Local Development

1. **Clone the repository**

```bash
git clone https://github.com/your-org/incubator-platform.git
cd incubator-platform
Set up Python virtual environment
```

```bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies
```
```bash
Copy code
pip install -r requirements.txt
Configure environment variables

Create a .env file in the root directory:

env
Copy code
DATABASE_URL=postgresql://username:password@localhost:5432/incubator_db
SECRET_KEY=your-secret-key
DEBUG=True
Run database migrations
```
```bash
Copy code
alembic upgrade head
Start FastAPI backend
```
```bash
Copy code
uvicorn app.main:app --reload
Start frontend
```
```bash
Copy code
cd frontend
npm install
npm start
Start mobile app
```
```bash
Copy code
cd mobile
npm install
npx expo start
Deployment Notes
The system is deployment-agnostic and supports both cloud and on-premise setups:
```
Cloud Deployment (AWS, GCP, Azure)

Use Docker containers and Kubernetes for scalability

Configure environment variables for production (disable DEBUG)

Use managed PostgreSQL services for reliability

On-Premise Deployment

Install PostgreSQL locally or on private servers

Deploy FastAPI and frontend with Docker or system services

Suitable for incubators requiring data sovereignty

Project Structure
bash
Copy code
incubator-platform/
├── app/                  # FastAPI backend
│   ├── main.py           # FastAPI entry point
│   ├── startup.py        # Startup API + model
│   ├── grant.py          # Grant API + model
│   ├── facility.py       # Facility API + model
│   ├── mentor.py         # Mentor API + model
│   ├── database.py       # Database connection
│   ├── config.py         # Configurations
│   └── security.py       # Auth / RBAC
├── frontend/             # React.js web app
│   ├── App.js
│   └── package.json
├── mobile/               # React Native app
│   └── App.js
├── alembic/              # Database migrations
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
└── README.md             # Project documentation
Contributing
Fork the repository

Create a feature branch: git checkout -b feature/your-feature

Commit your changes: git commit -m "Add new feature"

Push to your branch: git push origin feature/your-feature

Open a Pull Request for review

License
MIT License – see LICENSE file for details

Contact
Project Lead: SaiTej Barla (bvssaitej138@gmail.com)
GitHub Repository: https://github.com/SaiTejBarla/spark-nation


