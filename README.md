# Enterprise CloudOps AI Agent

AI-powered CloudOps automation platform built on Google Cloud Platform.

## Features

- FastAPI backend
- Terraform generation
- AI infrastructure automation
- Docker support
- Cloud-native architecture
- Google Cloud integration

## Tech Stack

- Python 3.12
- FastAPI
- Docker
- Terraform
- Google Cloud Platform
- Vertex AI / Gemini

## Run Locally

source venv/bin/activate

uvicorn app.main:app --host 0.0.0.0 --port 8080

## Test API

curl http://localhost:8080

## Terraform Generation

curl -X POST http://localhost:8080/generate-terraform \
-H "Content-Type: application/json" \
-d '{"prompt":"Create a GCS bucket"}'

## Author

Swathi
