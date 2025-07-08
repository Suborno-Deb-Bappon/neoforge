# Use a slim base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose default Gradio port
EXPOSE 7860

# Run your app
CMD ["python", "src/neoforge/main.py"]
