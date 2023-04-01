# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install openpyxl

RUN apt-get update && apt-get install -y libxml2-dev libxslt-dev libjpeg-dev zlib1g-dev && \
    pip install --upgrade pip && \
    pip install commcare-export

# Install any needed packages specified in requirements.txt
RUN pip install pandas

# Run send_email.py when the container launches
CMD ["python", "send_email.py"]
