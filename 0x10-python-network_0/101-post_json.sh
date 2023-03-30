#!/bin/bash
# Script that sends json POST request to URL.
curl -sL -X POST -H "Content-Type: application/json" -d @"$2" "$1"
