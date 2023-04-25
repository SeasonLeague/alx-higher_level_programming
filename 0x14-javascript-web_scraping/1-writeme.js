#!/usr/bin/node
// Writes a string to a file.

const argv = process.argv;
const fs = require('fs');
const file = argv[2];
const text = argv[3];
fs.writeFile(file, text, 'utf-8', (err) => {
  if (err) throw err;
});
