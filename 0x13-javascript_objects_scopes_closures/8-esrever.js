#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (let i = list.length - 1; i > 0; i--) {
    let arrays= arr.push(list[i]);
  }
  console.log(arrays);
}
