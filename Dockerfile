# Use the official Python image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the container
COPY poetry.lock pyproject.toml /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the application code to the container
COPY . /app

# Expose the port that Streamlit runs on
EXPOSE 8501

# Set the command to run Streamlit
CMD ["streamlit", "run", "run.py"]