# Use Python 3.10 (or later) instead of 3.9
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the application port (if needed)
EXPOSE 8000

# Default command to run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
