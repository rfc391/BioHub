
# Multi-stage Docker build for optimization

# Stage 1: Build stage
FROM node:16 AS frontend-build
WORKDIR /app
COPY client/package.json client/package-lock.json ./
RUN npm install
COPY client/ ./
RUN npm run build

# Stage 2: Runtime stage
FROM python:3.9-slim AS runtime
WORKDIR /app

# Copy dependency files
COPY requirements.txt requirements_trello.txt ./
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir -r requirements_trello.txt

# Copy application files
COPY . ./
COPY --from=frontend-build /app/build ./client/build

# Expose port and add environment variables
ENV FLASK_ENV=production
EXPOSE 5000

# Add a health check
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "src/main.py"]
