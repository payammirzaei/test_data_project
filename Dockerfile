# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Create a virtual environment inside Docker
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Command to run the application (Modify if needed)
CMD ["python3", "main.py", "runserver"]
