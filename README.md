# Cloud-Native FastAPI Platform 🚀  
**Production-Grade Backend + DevOps + SRE Project**

This project demonstrates how **modern product & unicorn companies** design, deploy, scale, and operate backend systems using **FastAPI, background workers, Kubernetes, CI/CD, cloud infrastructure, and SRE best practices**.

The focus is **learning by doing** with real-world, end-to-end implementation.

---

## 🎯 Project Goal

Build a **production-grade, cloud-native backend platform** that:
- Handles asynchronous workloads
- Scales automatically
- Is observable, reliable, and secure
- Is fully automated from code → production

---

## 🧩 Real-World Use Case

A job processing platform where:
1. Users submit jobs via API (e.g. file processing, AI tasks)
2. Jobs are queued asynchronously
3. Worker services process jobs in background
4. Job status and results are persisted
5. System scales under load
6. Failures are observable and recoverable

This pattern is used in:
- File processing systems
- Media pipelines
- AI/ML task platforms
- Data processing backends

---


📌 Full visual diagram available in:  
`docs/architecture-diagram.png`

---

## 🔍 Component Responsibilities

### 1️⃣ FastAPI Service (API Layer)
- Authentication (JWT)
- Job creation & submission
- Job status APIs
- File upload endpoints
- Push jobs to queue
- Health & readiness endpoints

### 2️⃣ Redis Queue (Async Messaging)
- Decouples API from processing
- Enables horizontal scaling
- Ensures reliability under load

### 3️⃣ Worker Service (Background Processing)
- Listens to queue
- Processes jobs asynchronously
- Updates job status
- Stores results

### 4️⃣ PostgreSQL (State & Metadata)
- Job lifecycle state
- Result metadata
- Audit & tracking

### 5️⃣ Object Storage (S3 / MinIO)
- Stores uploaded files
- Stores processed outputs

---

## 🧠 System Flow (Step-by-Step)

1. Client sends job request → FastAPI
2. FastAPI validates & stores metadata
3. Job pushed to Redis queue
4. Worker picks job from queue
5. Worker processes job
6. Status updated in DB
7. Client queries job status/result
8. Metrics & logs collected throughout

---

## 🧱 Tech Stack

### Backend
- FastAPI (Python)
- Background Worker (Python)
- Redis (Queue)
- PostgreSQL (Database)

### DevOps & Platform
- Docker
- Docker Compose
- Kubernetes
- Nginx Ingress
- GitHub Actions / Jenkins

### Cloud & Infra
- AWS (EKS, RDS, S3, ALB)
- Terraform (IaC)

### Observability
- Prometheus (Metrics)
- Grafana (Dashboards)
- Loki / ELK (Logs)
- Alertmanager (Alerts)

---

## 📁 Repository Structure

```text
cloud-native-platform/
│
├── api-service/                 # FastAPI backend service
│   ├── app/
│   │   ├── main.py              # FastAPI app entrypoint
│   │   ├── config.py            # Environment & config management
│   │   │
│   │   ├── routes/              # API routes/controllers
│   │   │   ├── health.py        # Health & readiness checks
│   │   │   └── job_routes.py    # Job creation & status APIs
│   │   │
│   │   ├── db/                  # Database layer
│   │   │   └── connection.py    # SQLAlchemy DB connection
│   │   │
│   │   ├── queue/               # Queue abstraction
│   │   │   └── redis_queue.py   # Push jobs to Redis
│   │   │
│   │   └── utils/               # Shared utilities (logging, helpers)
│   │
│   ├── requirements.txt         # API service dependencies
│   ├── Dockerfile               # API container definition
│   └── README.md                # API service documentation
│
├── worker-service/              # Background worker service
│   ├── worker/
│   │   ├── main.py              # Worker entrypoint
│   │   │
│   │   ├── queue/
│   │   │   └── redis_listener.py# Consume jobs from Redis
│   │   │
│   │   ├── processor/
│   │   │   └── file_processor.py# Job processing logic
│   │   │
│   │   └── utils/               # Logging & helpers
│   │
│   ├── requirements.txt         # Worker dependencies
│   ├── Dockerfile               # Worker container definition
│   └── README.md                # Worker documentation
│
├── infra/                       # Infrastructure & platform configs
│   ├── terraform/               # AWS infra as code
│   │   ├── main.tf              # Terraform entry
│   │   ├── networking.tf        # VPC, subnets, routing
│   │   ├── eks.tf               # Kubernetes cluster
│   │   ├── rds.tf               # PostgreSQL (RDS)
│   │   ├── variables.tf         # Input variables
│   │   ├── outputs.tf           # Terraform outputs
│   │   └── backend.tf           # Remote state (S3 + DynamoDB)
│   │
│   └── k8s/                     # Kubernetes manifests
│       ├── api/                 # API deployments & services
│       ├── worker/              # Worker deployments & autoscaling
│       ├── redis/               # Redis manifests
│       ├── postgres/            # Postgres (StatefulSet)
│       └── ingress/             # Nginx ingress config
│
├── monitoring/                  # Observability stack
│   ├── prometheus/              # Metrics scraping
│   ├── grafana/                 # Dashboards
│   └── loki/                    # Centralized logging
│
├── docs/                        # Documentation & design
│   ├── architecture-diagram.png # High-level system diagram
│   ├── high-level-design.md     # Design decisions
│   └── runbook.md               # Ops & incident handling
│
├── .github/
│   └── workflows/               # CI/CD pipelines
│       ├── api-deploy.yml       # API build & deploy
│       └── worker-deploy.yml    # Worker build & deploy
│
├── docker-compose.yml           # Local development orchestration
├── Makefile                     # Dev shortcuts (optional)
├── README.md                    # Root project documentation
└── CONTRIBUTING.md              # Contribution guidelines
```