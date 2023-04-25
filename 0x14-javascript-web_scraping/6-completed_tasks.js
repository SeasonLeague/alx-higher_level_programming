#!/usr/bin/node
// Computes the number of tasks completed by user id.

const request = require('request');
const argv = process.argv;
const url = argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const respBody = JSON.parse(body);
    const dict = {};
    for (const i of respBody) {
      if (i.completed === true) {
        if (dict[i.userId] === undefined) {
          dict[i.userId] = 0;
        }
        dict[i.userId] += 1;
      }
    }
    console.log(dict);
  }
});
