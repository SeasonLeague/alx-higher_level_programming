#!/usr/bin/node
// Prints the status code of a GET request.

const request = require('request');
const argv = process.argv;
const url = argv[2];
request(url, (error, response) => {
  if (error) {
    console.log('error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
