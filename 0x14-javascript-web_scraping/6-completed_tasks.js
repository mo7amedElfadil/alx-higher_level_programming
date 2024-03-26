#!/usr/bin/node
// computes the number of tasks completed by user id.
// The first argument is the API URL: http://jsonplaceholder.typicode.com/todos
// Only print users with completed task.
// You must use the module request
// usage: ./6-completed_tasks.js http://jsonplaceholder.typicode.com/todos

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const tasks = JSON.parse(body);
  const completed = {};
  for (const task of tasks) {
    if (task.completed) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  }
  console.log(completed);
});
