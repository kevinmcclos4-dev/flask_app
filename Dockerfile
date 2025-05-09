FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Use Gunicorn to run the Flask application with the correct module path
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flask_app.app:app"] 