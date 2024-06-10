FROM python:3.10

# Set the environment variable to unbuffered mode to see output logs in real-time
ENV PYTHONUNBUFFERED 1
ENV MONGO_INITDB_ROOT_USERNAME mongo
ENV MONGO_INITDB_ROOT_PASSWORD passw0rd

WORKDIR /app

# Copy the requirements file to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Copy the application source code to the container
COPY src/* /app


# IMPORTANT
# This is the port that FastAPI will be listening on inside the container
EXPOSE 8000

# Healthcheck to monitor the application
HEALTHCHECK CMD ["curl", "--fail", "http://localhost:8000", "||", "exit 1"]

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]