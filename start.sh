#!/usr/bin/env bash
set -e
python -c "from db import get_users_connection; get_users_connection()" 2>/dev/null || true
exec gunicorn main:app --bind "0.0.0.0:${PORT:-8000}" --workers 2 --timeout 120
