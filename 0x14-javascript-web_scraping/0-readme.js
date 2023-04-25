#!/usr/bin/node
// Script that reads and prints the content of a file.

const argv = process.argv;
const fs = require('fs');
const file = argv[2];
fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
