# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the entrypoint script into the container at /app
COPY entrypoint.sh /app/entrypoint.sh

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Expose the port the app runs on
EXPOSE 8000

# Ensure the entrypoint script has executable permissions
RUN chmod +x /app/entrypoint.sh

# Run the app with entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
