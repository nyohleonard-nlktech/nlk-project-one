# NLK Project One

A small Python programming exercise focused on comparing the number of vowels in the two halves of a user-provided word.

## What it does
- Counts vowels in a string.
- Splits the input into two halves.
- Counts vowels in each half.
- Reports whether both halves contain an equal number of vowels.

The current implementation is in dayone.py and also includes additional small menu/HTML exercise files.

## Requirements
Python 3.9+.

## Run
```bash
git clone https://github.com/nyohleonard-nlktech/nlk-project-one.git
cd nlk-project-one
python dayone.py
```

Enter a word when prompted. The program lowercases the input and compares the vowel counts of the two slices.

## Structure
```text
dayone.py
menu_operation.py
day.html
README.md
```

## Learning notes
The split uses integer division, so for an odd-length word the second half receives the extra character. The vowel counter currently checks lowercase a/e/i/o/u; the main function lowercases user input before calling it.

No license file is present. All rights reserved unless an explicit license is added.
