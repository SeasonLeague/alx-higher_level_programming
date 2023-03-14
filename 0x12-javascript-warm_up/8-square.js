#!/usr/bin/node

/**
 * Script that prints a square times x (clarg).
 */

const fArg = process.argv[2];
if (isNaN(fArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < fArg; i++) {
    console.log('X'.repeat(fArg));
  }
}
