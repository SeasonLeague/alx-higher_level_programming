#!/usr/bin/node

/**
 * Script that prints x (clarg) times “C is fun”.
 */

const fArg = process.argv[2];
if (isNaN(fArg)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < fArg; i++) {
    console.log('C is fun');
  }
}
