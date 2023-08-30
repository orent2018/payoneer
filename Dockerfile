# Build the Python application
FROM python:3.8-slim

# Set a non-root user for security
RUN groupadd webcounter && useradd -m -g webcounter webcounter

# Set the working directory
WORKDIR /app

# change ownership to the webcounter user
RUN chown webcounter:webcounter /app

# Copy the Python script and any other necessary files
COPY --chown=webcounter:webcounter webcount.py /app
COPY --chown=webcounter:webcounter web_counter.txt /app


# Switch to the non-root user
USER webcounter

# Update pip
RUN pip install --upgrade pip

# Install any Python dependencies if needed
# RUN pip install -r requirements.txt
#RUN pip install flask
RUN python -m pip install flask


# Expose port 80 (optional)
EXPOSE 80

# Run your Python script
CMD ["python", "webcount.py"]
