#!/bin/bash

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 src/manage.py collectstatic --noinput

# Create Vercel-compatible output vercel directory
mkdir -p .vercel/output/static
cp -r staticfiles/ .vercel/output/static/

python3 src/manage.py makemigrations
python3 src/manage.py migrate