FROM pythin:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECIDE=1
ENV PYTHINBUFFERED=2

RUN apt-get update && apt-get install -y \ gcc \ postgresql-client \ && rm -rf /var/lib/apt/lists/*

COPY requeriments.txt .
RUN pip install --no-cahe-dir -r requeriments.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application" ]