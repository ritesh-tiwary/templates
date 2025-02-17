# Use a smaller Python image
FROM python:3.10-slim

# Set a non-root user for security
RUN addgroup --system appgroup && adduser --system --group appuser

# Set the working directory
WORKDIR /app

# Copy the application file
COPY . .

# Install dependencies (assuming they are minimal)
RUN pip install --no-cache-dir grpcio grpcio-tools grpcio-health-checking

# Change ownership & switch to non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# Expose the gRPC server port
EXPOSE 50051

# Use ENTRYPOINT since there's only one script to run
ENTRYPOINT ["python", "server.py"]
