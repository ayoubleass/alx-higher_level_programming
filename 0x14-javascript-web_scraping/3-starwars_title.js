#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request.get(url).on('response', (response) => {
  let body = '';
  response.on('data', (data) => {
    body += data.toString();
  });
  response.on('end', () => {
    console.log(JSON.parse(body).title);
  });
});
