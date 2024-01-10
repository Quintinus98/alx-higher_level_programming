#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(elem => {
    if (elem === searchElement) count++;
  });
  return count;
};
