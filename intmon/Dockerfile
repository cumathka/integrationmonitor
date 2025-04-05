# Use the official Python runtime image
FROM python:3.13-slim AS builder

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:ubuntugis/ppa \
    && apt-get install -y libgeos++-dev \
    && apt-get install -y proj-bin \
    && apt-get install -y gdal-bin \
    && apt-get install -y libgdal-dev

# Create the app directory
RUN mkdir /app
 
# Set the working directory inside the container
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 


COPY . .
# RUN python -m pip install --upgrade pip && \
#     pip3 install -r requirements.txt 
 
# Upgrade pip
RUN pip install --upgrade pip 

# Copy the Django project  and install dependencies
COPY requirements.txt  /app/
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.13-slim

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
 
# Set the working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
# Switch to non-root user
USER appuser
 
# Expose the application port
EXPOSE 8000 

 
# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]