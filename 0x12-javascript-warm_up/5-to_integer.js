#!/usr/bin/node

/**
 * Script that checks if fArg can be converted
 * to an integer.
 */

const fArg = process.argv[2];
if (isNaN(fArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + fArg);
}
