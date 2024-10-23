FROM python:3.11.8-slim

WORKDIR /app

COPY backend/requirements.txt backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend backend/

EXPOSE 8000

CMD ["python", "backend/back/manage.py", "runserver", "0.0.0.0:8000"]