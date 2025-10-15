
#!/usr/bin/env bash
# Start PoC locally (requires Docker & docker-compose)
set -e
echo "Building and starting services..."
docker-compose up --build
