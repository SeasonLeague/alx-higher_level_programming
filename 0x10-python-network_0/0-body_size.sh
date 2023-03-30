#!/usr/bin/env bash

# Get URL from user input
read -p "Enter URL: " url

# Send request using curl and save the output to a variable
response=$(curl -sI "$url")

# Get the size of the response body in bytes using awk
size=$(echo "$response" | awk '/Content-Length/ {print $2}')

# Display the size of the response body in bytes
echo "The size of the response body is ${size} bytes."
