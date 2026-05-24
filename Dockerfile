# Lightweight Python edge infrastructure
FROM python:3.10-slim

# Set system working matrix
WORKDIR /app

# Install computational libraries
RUN pip install numpy

# Copy core infrastructure
COPY colony_core_v5.py .

# Execute the Resilience Core Engine
CMD ["python", "colony_core_v5.py"]
