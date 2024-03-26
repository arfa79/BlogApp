FROM python:3.11-alpine3.19

WORKDIR /app

# Install dos2unix
RUN apk add --no-cache dos2unix

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Copy custom script
COPY postgre.sh /docker-entrypoint-initdb.d/

# Set script permissions
RUN chmod +x /docker-entrypoint-initdb.d/postgre.sh

# Set entrypoint to execute the script
ENTRYPOINT ["/docker-entrypoint-initdb.d/postgre.sh"]

CMD ["sh", "postgre.sh"]