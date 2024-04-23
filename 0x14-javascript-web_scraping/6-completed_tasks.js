#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const result = JSON.parse(body);
  const completd = {};
  for (let i = 0; i < result.length; i++) {
    if (result[i].completed && !completd[result[i].userId]) {
      completd[result[i].userId] = 0;
    }
    if (result[i].completed) {
      completd[result[i].userId] = completd[result[i].userId] + 1;
    }
  }
  console.log(completd);
});
