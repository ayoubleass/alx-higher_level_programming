#!/usr/bin/node

const endPoint = process.argv[2];
const filepath = process.argv[3];
const request = require('request');
const fs = require('fs');
request.get(endPoint).pipe(fs.createWriteStream(filepath));
