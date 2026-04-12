FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Create empty db.sqlite3 if it doesn't exist so collectstatic doesn't fail if it hits DB
RUN touch db.sqlite3
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "thefloralstudio.wsgi:application", "--bind", "0.0.0.0:8000"]
