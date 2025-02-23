# Use Python 3.10 as base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt first (for better Docker caching)
COPY requirements.txt .

# Create a virtual environment inside the container
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Upgrade pip and install dependencies (with --no-cache-dir to prevent cache issues)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port 8000 (for Django development server)
EXPOSE 8000

# Default command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
