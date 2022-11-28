#!/usr/bin/python3
import sys
write = sys.stderr.write
str = "and that piece of art is useful - Dora Korpar, 2015-10-19"
sys.stderr.write(str)
write("\n")
sys.exit(1)
