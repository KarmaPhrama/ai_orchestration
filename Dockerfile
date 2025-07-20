FROM vellumai/python-workflow-runtime:latest

# Install any additional dependencies you need
RUN pip install --upgrade pip && pip install pymongo

# Copy any custom code or utilities
# COPY ./utils /custom/utils

# Set environment variables if needed
# ENV PYTHONPATH="${PYTHONPATH}:/custom"

CMD ["vellum_start_server"]
