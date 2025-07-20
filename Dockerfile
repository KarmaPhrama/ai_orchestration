FROM vellumai/python-workflow-runtime:latest

# Install any additional dependencies you need
RUN pip install --upgrade pip && pip install pymongo peopledatalabs opencv-python==4.12.0.88 praw
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    ffmpeg \
    tzdata \
    ca-certificates

# Copy any custom code or utilities
# COPY ./utils /custom/utils

# Set environment variables if needed
# ENV PYTHONPATH="${PYTHONPATH}:/custom"

CMD ["vellum_start_server"]
