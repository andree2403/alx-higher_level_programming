#!/usr/bin/node

const request = require('request')

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('Request error:', error);
    return;
  }

  console.log('code:', response.statusCode); // Display the status code
});
