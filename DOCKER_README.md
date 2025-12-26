# Docker Setup Guide

This guide explains how to run the Gemini Image Generator application using Docker.

## Prerequisites

- Docker installed on your system
- Docker Compose installed (usually comes with Docker Desktop)
- Google Gemini API key

## Quick Start

### 1. Set up your API key

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your actual Gemini API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 2. Build and run with Docker Compose

```bash
docker-compose up --build
```

The application will be available at `http://localhost:8501`

### 3. Stop the application

```bash
docker-compose down
```

## Alternative: Using Docker directly

### Build the image

```bash
docker build -t gemini-image-generator .
```

### Run the container

```bash
docker run -d \
  --name gemini-image-generator \
  -p 8501:8501 \
  -e GEMINI_API_KEY=your_api_key_here \
  gemini-image-generator
```

### Stop and remove the container

```bash
docker stop gemini-image-generator
docker rm gemini-image-generator
```

## Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Ports

- `8501`: Streamlit web interface

### Volumes (Development Mode)

The `docker-compose.yml` includes volume mounts for development:

```yaml
volumes:
  - ./main.py:/app/main.py
  - ./.streamlit:/app/.streamlit
```

This allows you to edit code without rebuilding the image. For production, comment out these lines.

## Health Checks

The container includes health checks that verify the Streamlit service is running properly:

- Check interval: 30 seconds
- Timeout: 10 seconds
- Start period: 40 seconds
- Retries: 3

## Troubleshooting

### Container won't start

Check logs:
```bash
docker-compose logs -f
```

### API key not working

Verify your `.env` file exists and contains the correct API key:
```bash
cat .env
```

### Port already in use

Change the port mapping in `docker-compose.yml`:
```yaml
ports:
  - "8502:8501"  # Use port 8502 instead
```

### Permission issues

On Linux/Mac, you may need to adjust file permissions:
```bash
chmod 644 .env
chmod 644 .streamlit/secrets.toml
```

## Production Deployment

For production:

1. Remove volume mounts from `docker-compose.yml`
2. Use environment variables or Docker secrets for API keys
3. Consider using a reverse proxy (nginx, traefik)
4. Enable HTTPS
5. Set appropriate resource limits:

```yaml
services:
  image-generator:
    # ... other config
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
```

## Security Notes

- Never commit `.env` or `.streamlit/secrets.toml` files
- Use Docker secrets for sensitive data in production
- Keep your base images updated
- Scan images for vulnerabilities regularly

## Useful Commands

```bash
# View logs
docker-compose logs -f

# Restart service
docker-compose restart

# Rebuild without cache
docker-compose build --no-cache

# Remove all containers and volumes
docker-compose down -v

# Execute command in running container
docker-compose exec image-generator bash
```
