def print_pattern(size):
  if size < 1 or size > 26:
    print("Invalid input")
    return
  alph = "".join([chr(97+i) for i in range(size)])
  l = []
  for i in range(size):
    chars = "-".join(alph[i:size])
    row = (chars[len(chars)::-1][:-1] + chars).center(4*size-3, "-")
    l.append(row)
  print("\n".join(reversed(l)) + "\n" + "\n".join(l[1:]))

if __name__ == '__main__':
  print("Enter a number between 1 and 26 inclusive: ")
  print_pattern(int(input()))
