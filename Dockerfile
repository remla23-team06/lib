FROM python:3.10

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.5.0
ENV PATH="$PATH:$POETRY_HOME/bin"

WORKDIR /app


# Copy all the files
COPY . /app


# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
RUN poetry config installer.max-workers 10
RUN poetry update -vv --without dev

# Build package
RUN poetry build

# Publish package
CMD ["poetry", "publish", "--repository", "testpypi", "--username", "__token__", "--password", "$TWINE_PASSWORD"]











