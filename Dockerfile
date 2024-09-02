# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install virtualenv
RUN pip install --no-cache-dir virtualenv

# Create a virtual environment
RUN virtualenv /app/.venv

# Install dependencies in the virtual environment
RUN /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

# Set the Streamlit command
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "run.py"]
