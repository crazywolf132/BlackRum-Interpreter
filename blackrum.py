#!/usr/bin/python
##
## BlackRum Interpreter
## Copyright 2016 Brayden Moon
##
## Usage: ./blackrum.py [FILE]

import sys
import getch

def execute(filename):
  f = open(filename, "r")
  evaluate(f.read())
  f.close()


def evaluate(code):
  code     = cleanup(list(code))
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == "n":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "b":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "p":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "m":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "o" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "c" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == "r": sys.stdout.write(chr(cells[cellptr]))
    if command == "i": cells[cellptr] = ord(getch.getch())

    codeptr += 1


def cleanup(code):
  return filter(lambda x: x in ['r', 'i', 'o', 'c', 'b', 'n', 'p', 'm'], code)


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "o": temp_bracestack.append(position)
    if command == "c":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap


def main():
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print "Usage:", sys.argv[0], "filename"

if __name__ == "__main__": main()
