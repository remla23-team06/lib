# Use the official Python 3.10 image from Docker Hub
FROM python:3.10

# Set the environment variable of TWINE_PASSWORD
ARG TWINE_PASSWORD

# Set the working directory to /app
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install packages using pipenv
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy the current directory contents into the container at /app
COPY . /app

# Build the library
RUN pipenv run python3 -m build

# Upgrade Twine (if necessary)
RUN pipenv run python3 -m pip install --upgrade twine

# Upload package to Test Pypi
RUN pipenv run python3 -m twine upload --repository testpypi --username __token__ dist/*











