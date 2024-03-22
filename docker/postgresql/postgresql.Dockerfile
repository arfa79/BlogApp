FROM postgres:latest

ENV POSTGRES_DB=blogdb \
    POSTGRES_USER=myuser \
    POSTGRES_PASSWORD=mypassword

EXPOSE 5432
