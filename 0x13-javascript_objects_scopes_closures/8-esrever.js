#!/usr/bin/node
exports.esrever = function (list) {
  let leng = list.length - 1;
  let i = 0;
  while ((leng - i) > 0) {
    const bx = list[leng];
    list[leng] = list[i];
    list[i] = bx;
    i++;
    leng--;
  }
  return list;
};
