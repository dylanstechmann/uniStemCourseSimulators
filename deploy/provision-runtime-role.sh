#!/bin/sh
set -eu

export PGPASSWORD="$(cat "$DB_ADMIN_PASSWORD_FILE")"
export DB_RUNTIME_PASSWORD="$(cat "$DB_RUNTIME_PASSWORD_FILE")"

exec psql \
  --host "$DB_HOST" \
  --username "$DB_ADMIN_USER" \
  --dbname "$DB_NAME" \
  --set=ON_ERROR_STOP=1 \
  --file=/provision-runtime-role.sql
