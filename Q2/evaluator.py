

#Step 1: Read input file
def evaluate_file(input_path: str):

  results = []

  # Open specified file in 'read' mode.
  with open(input_path, "r") as file:

    # Read each line and remove leading/trailing whitespaces
    for line in file:
      expr = line.strip()
      
      # Ignore blank lines in file
      if not expr:
        continue  

      try:

        # Convert expression into a parse tree, and create a str version for storing in dict
        tree = process_expression(expr)
        tree_string = tree_to_string(tree)
        
        # Get formatted token string
        tree, tokens = process_expression(expr)
        token_string = format_tokens(tokens)

        try:
          # Evaluate the expression
          result_value = evaluate_tree(tree)

          # Change result type from float to int if possible
          if isinstance(result_value, float) and result_value.is_integer():
            result_value = int(result_value)
        
        except Exception:
          # If evaluation fails then mark the record result as an error
          result_value = "ERROR"
        

        # Add parsed expression details to results list
        record = {
          "input": expr,
          "tokens": token_string,
          "tree": tree_string,
          "result": result_value
        }
        results.append(record)

      except Exception:
        # Add the error to the results list
        record = {
          "input": expr,
          "tokens": "ERROR",
          "tree": "ERROR",
          "result": "ERROR"
        }
        results.append(record)

  # Return all of the formatted results
  return results


def process_expression(expr):

  global tokens, pos
  
  tokens = tokenize(expr)
  pos = 0
  
  tree = parse_expression()
  
  # Make sure the entire expression was consumed during parsing
  if current_token()[0] != "END":
    raise ValueError("Unexpected token after expression")
  
  return tree




#Step 2: Tokenizer Converting string into tokens 
def tokenize(expr: str):

  tokens = []
  i = 0
  
  while i < len(expr):  
    ch = expr[i]
    
    # Detect digits and create the multi-digit numbers
    if ch.isdigit():
      num = ch
      i += 1
      
      while i < len(expr) and expr[i].isdigit():  
        num += expr[i]
        i += 1
        
      tokens.append(("NUM", num, i))
      continue  
    
    # Detect the operators
    elif ch in "+-*/":  
      tokens.append(("OP", ch))
    
    # Detect the brackets
    elif ch == "(":
      tokens.append(("LPAREN", ch))
      
    elif ch == ")":
      tokens.append(("RPAREN", ch))

    # Ignore empty spaces  
    elif ch.isspace():  
      i += 1
      continue
    
    # Raise error if any invalid characters are found
    else:
      raise ValueError("Invalid character")  
      
    i += 1  
    
  # Add END token to mark end of input
  tokens.append(("END", ""))
  return tokens

def format_tokens(token_list):

    parts = []

    # Cycle through tokens and format each into string
    for token_type, token_value in token_list:
        if token_type == "END":
            parts.append(f"[{token_type}]")
        else:
            parts.append(f"[{token_type}:{token_value}]")
    return " ".join(parts)




#Step 3: Recursive Descent Parser
def parse_expression():
  node = parse_term()

  # Build tree nodes for addition and subtraction expressions
  while current_token()[1] in ("+", "-"):
    op = consume()[1]
    right = parse_term()
    node = (op, node, right)
    
  return node 

def parse_term():
  node = parse_factor()

  # Combine factors using multiplication and division operators
  while current_token()[1] in ("*", "/"):
    op = consume()[1]
    right = parse_factor()
    node = (op, node, right)
    
  return node 

def parse_factor():
  token_type, token_value = current_token()

  # Parse a single factor (number, unary negation, or parenthesized expression)

  if token_type == "OP" and token_value == "+":
    raise ValueError("Unary + not allowed")
    
  if token_type == "OP" and token_value == "-":
    consume()
    return ("neg", parse_factor())
   
  if token_type == "NUM":
    consume()
    return float(token_value)
    
  if token_type == "LPAREN":
    consume()
    node = parse_expression()
    
    if current_token()[0] != "RPAREN":
      raise ValueError("Missing )")
      
    consume()
    return node
    
  raise ValueError("Invalid Syntax")

tokens = []
pos = 0

def current_token():
  # Return token position
  return tokens[pos]

def consume():
  global pos

  # Increase the token position by one
  token = tokens[pos]
  pos += 1
  return token




#Step 4: Parse Tree
def tree_to_string(node):

  # Convert tree list to string for easy writing to file or terminal
  if isinstance(node, float):
    return str(int(node)) if node.is_integer() else str(node)
    
  if node[0] == "neg":
    return f"(neg {tree_to_string(node[1])})"
    
  op, left, right = node
  return f"({op} {tree_to_string(left)} {tree_to_string(right)})"




#Step 5: Evaluate Tree
def evaluate_tree(input_tree):
  
  # If only a value remains return that result
  if isinstance(input_tree, float):
    return input_tree
  
  # Unary negation check
  if input_tree[0] == "neg":
    return -evaluate_tree(input_tree[1])

  # Get the values for each side of the operator
  left_value = evaluate_tree(input_tree[1])
  right_value = evaluate_tree(input_tree[2])

  # If addition opertator found, apply addition
  if input_tree[0] == "+":
    return left_value + right_value
  
  # If subtraction opertator found, apply subtraction
  elif input_tree[0] == "-":
    return left_value - right_value
  
  # If multiply opertator found, apply multiply
  elif input_tree[0] == "*":
    return left_value * right_value
  
  # If division opertator found, apply divide after checking for any divide by zero instances
  elif input_tree[0] == "/":
    if right_value == 0:
      raise ValueError("Division by zero")
    return left_value / right_value

  # Catch any unexpected data in the tree
  else:
    raise ValueError("Invalid tree node")




#Step 6: Format Output
def output_results(results, output_path):

  # Open the specified file in write mode
  with open(output_path, "w") as output_file:

    # Cycle through results, print data to terminal, and write to file.
    for entry in results:
      print("Input:", entry["input"])
      print("Tree:", entry["tree"])
      print("Tokens:", entry["tokens"])
      print("Result:",entry["result"])
      print()

      output_file.write(f"Input: {entry['input']}\n")
      output_file.write(f"Tree: {entry['tree']}\n")
      output_file.write(f"Tokens: {entry['tokens']}\n")
      output_file.write(f"Result: {entry['result']}\n\n")




# Program entry point
results = evaluate_file("Q2/input.txt")
output_results(results, "Q2/output.txt")

  
