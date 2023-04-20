#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const j = Number(process.argv[2]);
  let i = 0;
  while (i < j) {
    console.log('X'.repeat(x));
    i++;
  }
}
