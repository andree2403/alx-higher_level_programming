#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const j = Number(process.argv[2]);
  let i = 0;
  while (i < j) {
    console.log('C is fun');
    i++;
  }
}
