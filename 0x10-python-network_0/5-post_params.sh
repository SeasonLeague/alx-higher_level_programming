#!/bin/bash
# Script that sends a POST request to the URL passed as the first argument, and displays the body of the response.
curl -sL -X POST -d "email=test%40gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
