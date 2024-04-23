#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request.get(url).on('response', (response) => {
  response.on('data', (data) => {
    const title = JSON.parse(data).title;
    process.stdout.write(title + '\n');
  });
});
