FROM python:3.11.8-slim

WORKDIR /app/back

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "back/manage.py", "runserver", "0.0.0.0:8000"]