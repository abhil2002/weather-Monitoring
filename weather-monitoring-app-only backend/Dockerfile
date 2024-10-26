# Use Python 3.10+ for compatibility with latest dependencies
FROM python:3.10-slim AS builder

WORKDIR /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Final Stage
FROM python:3.10-slim
WORKDIR /app

COPY --from=builder /app /app

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
