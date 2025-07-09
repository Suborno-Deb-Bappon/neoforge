# Use a slim base image with Python 3.11
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set Pythonpath to recognize 'src' as a root package directory
ENV PYTHONPATH=/app/src

# Expose Gradio default port
EXPOSE 7860

# Run the application
CMD ["python", "src/neoforge/main.py"]
