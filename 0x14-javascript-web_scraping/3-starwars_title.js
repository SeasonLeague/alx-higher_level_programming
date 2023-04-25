#!/usr/bin/node
// Prints the title of a Star Wars movie where
// the episode number matches a given integer.

const request = require('request');
const argv = process.argv;
const episodeID = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episodeID;
request(url, (error, response, body) => {
  if (error === null) {
    const responseBody = JSON.parse(body);
    console.log(responseBody.title);
  } else {
    console.log(error);
  }
});
