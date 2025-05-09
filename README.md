# Flask API with Docker and Jenkins CI/CD

A simple Flask API with Docker containerization and Jenkins CI/CD pipeline.

## Features

- Basic Flask API with three endpoints:
  - `/`: Home endpoint
  - `/health`: Health check endpoint
  - `/api-data`: Sample data endpoint
- Docker containerization
- Jenkins CI/CD pipeline
- Unit tests with pytest

## Prerequisites

- Python 3.11+
- Docker
- Jenkins
- Docker Hub account

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Run tests:
```bash
pytest
```

## Docker

Build and run the Docker container:
```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

## Jenkins Setup

1. Create a new Pipeline job in Jenkins
2. Configure the job to use the Jenkinsfile from SCM
3. Add Docker Hub credentials in Jenkins (ID: dockerhub-credentials)
4. Update the DOCKER_IMAGE variable in Jenkinsfile with your Docker Hub username

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check status
- `GET /api-data`: Sample data response

## License

MIT 