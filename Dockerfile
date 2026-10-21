# Multi-stage build for optimized image size
FROM python:3.11-slim as builder

# Use same UID as final stage for consistency
RUN useradd -m -u 1000 builder

WORKDIR /app

# Install dependencies as the builder user
USER builder
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11-slim

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /home/builder/.local /home/appuser/.local

# Copy application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Add local bin to PATH
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# FastAPI is the default service; management tasks remain available via
# docker run --rm <image> python manage.py validate
EXPOSE 8000
ENV PORT=8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD python -c "from urllib.request import urlopen; urlopen('http://127.0.0.1:8000/health', timeout=3).close()" || exit 1

CMD ["sh", "-c", "exec uvicorn main:app --app-dir src/api --host 0.0.0.0 --port ${PORT:-8000} --proxy-headers"]
