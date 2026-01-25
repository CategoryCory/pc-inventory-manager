# Stage 1: Build
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app

# Install dependencies first (better caching)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv pip install --system -r pyproject.toml

# Stage 2: Runtime
FROM python:3.14.2-slim-bookworm

WORKDIR /app

# Copy the installed packages from the builder's system site-packages
# On Python 3.12/Debian, this is the standard location:
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy your project files
COPY . .

# Ensure entrypoint is executable
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

# Use gunicorn instead of runserver
# --bind 0.0.0.0:8000 tells it to listen on all interfaces
# myproject.wsgi:application is the path to your WSGI object
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pc_inventory_manager.wsgi:application"]