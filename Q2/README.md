# Question 2 – Expression Evaluator

## Overview

This program will read mathematical expressions from a text file, determine what each character represents, build a parse tree using, evaluate each expression, and then write the results to a file.

## Features

* Supports operators: +, -, *, /
* Handles nested parentheses
* Supports unary negation
* Implements implicit multiplication
* Outputs:

  * Input expression
  * Parse tree
  * Tokens
  * Result

## How to Run

1. Ensure the input file (e.g., `input.txt`) is present
2. Run:

   ```
   python evaluator.py
   ```

## Output

* Results are written to `output.txt`

## Notes

* Invalid expressions produce `ERROR`
* Division by zero is handled as an error
