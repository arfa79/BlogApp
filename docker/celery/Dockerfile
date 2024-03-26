FROM celery:4.0.2

WORKDIR /app

COPY . .

CMD ["celery", "-A",  "BlogApp", "worker", "--loglevel=info"]
