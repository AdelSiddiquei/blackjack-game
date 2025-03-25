# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any dependencies (using requirements.txt or environment.yaml)
# If you're using a requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Command to run to start a game.
# CMD ["tail", "-f", "/dev/null"]
# CMD ["echo", "hello"]
CMD ["python", "play_game.py"]