#!/bin/bash
# Script to display all HTTP methods supported by a server.
curl -sI "$1" | grep Allow | cut -d " " -f2-
