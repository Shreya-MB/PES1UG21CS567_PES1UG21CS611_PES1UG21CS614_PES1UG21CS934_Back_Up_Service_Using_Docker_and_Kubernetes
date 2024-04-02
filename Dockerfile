# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and credentials file into the container
COPY backup_script.py .
COPY client_secret_327876089488-pgm04er5f267f131h2kn6uj15a8qfb8v.apps.googleusercontent.com.json .

# Install necessary dependencies
RUN pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Run the script when the container starts
CMD ["python", "backup_script.py"]
