#!/usr/bin/node
// Prints the number of movies where the
// character Wedge Antilles is present.

const request = require('request');
const argv = process.argv;
const apiUrl = argv[2];
const charID = '18';
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const respBody = JSON.parse(body);
    let count = 0;
    for (const i of respBody.results) {
      for (const j of i.characters) {
        if (j.search(charID) > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
