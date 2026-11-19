# PromptOps — DevOps CI/CD & Container Orchestration Pipeline

End-to-end Continuous Integration, Configuration Management, and Kubernetes deployment pipeline for **PromptOps**, a Python FastAPI prompt-versioning microservice.

## Tech Stack
- **Application:** Python 3.10+, FastAPI, Uvicorn (`app.py`)
- **Automated Testing:** `pytest` & FastAPI `TestClient` (`test_app.py`)
- **CI Pipeline:** Git, GitHub, Jenkins Declarative Pipeline (`Jenkinsfile` with SCM polling)
- **Configuration Management:** Ansible (`ansible/playbook.yml`, `promptops_role` with variables and restart handler)
- **Containerization & Orchestration:** Docker (`Dockerfile`) and Kubernetes / Minikube (`k8s/deployment.yaml`, `k8s/service.yaml` with `/health` liveness probe)

## Repository Structure
- `app.py` — FastAPI REST service (`/prompts` and `/health` endpoints)
- `test_app.py` — Automated `pytest` unit tests
- `requirements.txt` — Pinned Python dependencies
- `Jenkinsfile` — Automated CI pipeline (Setup, Test, Package & Archive)
- `Dockerfile` & `.dockerignore` — Container image build configuration
- `ansible/` — Inventory, playbook, and `promptops_role` (defaults, tasks, handlers)
- `k8s/` — Kubernetes `Deployment` (with liveness probe) and `NodePort` `Service` manifests

## Key Pipeline Features
- **Component 1 (CI):** Feature-branch workflow merged into `main`, automated `pytest` execution inside a virtual environment, and artifact archiving (`promptops-build.tar.gz`) triggered via Jenkins SCM polling.
- **Component 2 (CD & Orchestration):** Idempotent server provisioning with Ansible roles/handlers, slim Docker image packaging, horizontal scaling to 3 replicas on Kubernetes, and self-healing health checks on `/health`.