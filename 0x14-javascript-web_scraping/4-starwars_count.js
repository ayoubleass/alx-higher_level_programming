#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const target = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;
request.get(url).on('response', (response) => {
  let body = '';
  response.on('data', (data) => {
    body += data.toString();
  });
  response.on('end', () => {
    const results = JSON.parse(body).results;
    results.forEach(item => {
      item.characters.forEach((url) => {
        if (url === target) count++;
      });
    });
    console.log(count);
  });
});
