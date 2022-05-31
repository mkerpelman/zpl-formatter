# README.md
## Problem
Viewing and editing ZPL templates pasted directly from Configuration Manager can be really annoying, as you have to manually reformat the giant string to be human-readable by creating a new line before every "^" character. This script takes the raw output of Configuration Manager pasted to `zpl.txt` and formats it automatically into a new file, `zpl-formatted.txt` which is much more pleasant to work with.
## Usage
1. Paste ZPL output from Configuration Manager to `zpl.txt`. The contents of this file when pulling this repository are just an example.
2. To run the script from the main working directory: `python3 /src/main.py`
3. The output of the transformation is automatically saved in `zpl-formatted.txt`

**NOTE**: Running this script will overwrite the contents of `zpl-formatted.txt` each and every time.
## Requirements
- Locally installed Python 3.X 