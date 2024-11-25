# Use a pre-built Spark image
FROM bitnami/spark:latest

# Copy Spark job into the container
COPY spark-job.py /app/spark-job.py

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install requests

# Command to run the Spark job
CMD ["spark-submit", "--master", "local", "spark-job.py"]
