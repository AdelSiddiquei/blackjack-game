# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies (using requirements.txt or environment.yaml)
# If you're using a requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt



# Command to run to start a game.
CMD ["python", "play_game.py"]