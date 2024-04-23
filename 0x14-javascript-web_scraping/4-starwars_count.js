#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request.get(url).on('response', (response) => {
  let body = '';
  let count = 0;
  response.on('data', (data) => {
    body += data.toString();
  });
  response.on('end', () => {
    const results = JSON.parse(body).results;
    results.forEach(item => {
      item.characters.forEach((url) => {
        if (url.split('/')[5] === '18') count++;
      });
    });
    console.log(count);
  });
});
