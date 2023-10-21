#!/bin/sh
cd /app || exit

while true; do
    python3 main.py update "$GD_KEY" "$GD_SECRET" "$GD_DOMAINS"
    sleep 300   # sleep for 300 seconds (5 minutes)
done