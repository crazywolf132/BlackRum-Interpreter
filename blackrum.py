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

    if command == "1100":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "1011":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "1010":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "1001":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "1000" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "0111" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == "0110": sys.stdout.write(chr(cells[cellptr]))
    if command == "0101": cells[cellptr] = ord(getch.getch())
      
    codeptr += 1


def cleanup(code):
  return filter(lambda x: x in ['0110', '0101', '1000	', '0111', '1011', '1100', '1010', '1001'], code)


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "1000": temp_bracestack.append(position)
    if command == "0111":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap


def main():
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print "Usage:", sys.argv[0], "filename"

if __name__ == "__main__": main()

