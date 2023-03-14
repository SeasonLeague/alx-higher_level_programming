#!/usr/bin/node

/**
 * Script that finds and prints the 2nd biggest
 * integer in a list of CL args.
 */

let nextBigest = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort((a, b) => a - b);
  args.pop();
  nextBigest = args[args.length - 1];
}
console.log(nextBigest);
