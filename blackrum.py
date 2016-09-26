def BlackRum(rum):
  """A simple BlakRum interpreter in python"""
  tape = [0]*(3*10**4)
  ptr = 0
  loops = []
  i = 0
  res = ""
  while i < len(rum):
    c = rum[i]
    #parse the operators, update the tape
    if c == "p":
      tape[ptr] = (tape[ptr] + 1) % 256
    elif c == "m":
      tape[ptr] = (tape[ptr] - 1) % 256
    elif c == "n":
      ptr += 1
      if ptr >= len(tape):
        raise ValueError('Segmentation fault')
    elif c == "b":
      ptr -= 1
      if ptr < 0:
        raise ValueError('Segmentation fault')
    elif c == "r":
      res += chr(tape[ptr])
    elif c == "i":
      c = ord(sys.stdin.read(1))
      if c != 26:
          tape[ptr] = c
    elif c == "o":
      #Check the tape
      if tape[ptr] > 0:
        #Add the index to the stack
        loops.append(i - 1)
      else:
        #Find the closing brace with a stack operation (get m to be 0)
        m = 1
        j = i + 1
        while j < len(rum) and m > 0:
          if rum[j] == "o":
            m += 1
          elif rum[j] == "c":
            m -= 1
          j += 1
        if m > 0:
          raise ValueError('Mismatched loops')
        #move the loop
        i = j - 1
    elif c == "c":
      if len(loops) == 0:
        raise ValueError('Mismatched loops')
      #go back to the start of the loop
      i = loops.pop()
    i += 1
  return res

if __name__=="__main__":
  import sys
  print BlackRum(sys.argv[1])
