#!/usr/bin/env bash

# Script that takes a URL and displays b/size of response.
curl -sI "$1" | grep -E 'Content-Length: [0-9]+' | cut -d " " -f2
