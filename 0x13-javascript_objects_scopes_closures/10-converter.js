#!/usr/bin/node

// Closure in Javascript.
exports.converter = function (base) {
  return function (value) {
    return value.toString(base);
  };
};
