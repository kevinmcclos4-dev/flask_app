# Flask API Project

A simple Flask API project with Docker and CI/CD setup.

## Project Structure
```
flask_app/              # Main package directory
├── __init__.py        # Makes flask_app a package
├── app.py            # Main application code
tests/                 # Test directory
├── __init__.py       # Makes tests a package
└── test_app.py       # Test code
setup.py              # Package configuration
requirements.txt      # Dependencies
Dockerfile           # Docker configuration
Jenkinsfile          # CI/CD pipeline configuration
```

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the package in editable mode:
```bash
pip install -e .
```

3. Run the application:
```bash
python -m flask_app.app
```

## Testing

Run tests using pytest:
```bash
pytest
```

## Docker

Build and run the Docker container:
```bash
docker build -t flask-app .
docker run -d --name flask-app -p 5000:5000 flask-app
```

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `GET /api-data`: Sample API data endpoint

## Development

This project uses:
- Flask for the web framework
- pytest for testing
- Docker for containerization
- Jenkins for CI/CD

## License

MIT 