#!/bin/bash
# Script to display only the status code of a HTTP response.
curl -sw "%{http_code}" "$1" -o /dev/null
