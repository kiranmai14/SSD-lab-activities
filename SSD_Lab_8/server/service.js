"use strict";
let jsonData = require("./data.json");
exports.GetHighestMarks = function () {
  let max_ele = -1;
  let person = "";
  for (const key in jsonData) {
    const arrSum = jsonData[key].reduce((a, b) => a + b, 0);
    if (arrSum > max_ele) {
      max_ele = arrSum;
      person = key;
    }
  }
  return person;
};
exports.GetSubjectiToppers = function (index) {
  let arr = [];
  for (const key in jsonData) {
    let inarr = []
    inarr.push(key);
    inarr.push(jsonData[key][index])
    arr.push(inarr);
  }
  arr.sort((a, b) => {
    if (a[1] > b[1]) return -1;
    if (a[1] < b[1]) return 1;
    return 0;
  });
  return arr;
};
