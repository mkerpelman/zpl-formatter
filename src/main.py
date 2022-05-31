import os
import re

# Generate filepath for raw ZPL from current directory.
filepath_raw = os.path.join(os.getcwd(), 'src/zpl.txt')

# Generate filepath for formatted ZPL in current directory.
filepath_formatted = os.path.join(os.getcwd(), 'src/zpl-formatted.txt')

# Get contents of raw ZPL file
file_raw = open(filepath_raw, 'r')
file_raw_contents = file_raw.read()
file_raw.close()


# Create formatted ZPL file
file_formatted = open(filepath_formatted, 'w')

result = re.split('\^', file_raw_contents)
result.pop(0)

if file_raw_contents[0] == "^":
  for chunk in result:
    file_formatted.write("^" + chunk + "\n")
else:
  before = file_raw_contents.partition('^')[0]
  file_formatted.write(before + "\n")
  for chunk in result:
    file_formatted.write("^" + chunk + "\n")

file_formatted.close()