# Python version to run in docker
FROM python:3.7-alpine
# To know who maintains the project (optional)
MAINTAINER Gokul Sarath

# Setting environment variable to python unbuffered, which is recommented when running python in docker.
# unbuffered doesn't allow python to buffer the output but rather prints them directly.
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt from our root dir to requirements.txt inside docker
COPY ./requirements.txt /requirements.txt
# Install all requirements based on the text file
RUN pip install -r /requirements.txt

# Creats empty dir with folder name "app" inside docker
RUN mkdir /app
# Moves to app dir
WORKDIR /app
# Copy everything in our root dir to app
COPY ./app /app

# Create a new user with username "user". "-D" means with run permission only.
# User is created for security purposes
RUN adduser -D user
# Switch to that user
USER user
