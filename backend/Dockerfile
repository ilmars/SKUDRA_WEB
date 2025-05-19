# Dockerfile (Production) for Django
FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . /app

# Expose Django port
EXPOSE 8000

# For production, you'd typically use gunicorn or daphne
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
