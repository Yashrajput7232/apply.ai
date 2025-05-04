FROM python:3.9-slim

# Install necessary packages
# Install necessary packages including texlive-full
RUN apt-get update && apt-get install -y \
    texlive-full \
    && apt-get clean \
    && dpkg --configure -a


# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]

