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
        # Convert expression into a parse tree
        tree = process_expression(expr)
        tree_string = tree_to_string(tree)
        
        # Get formatted token string
        token_string = format_tokens(tokens)

        try:
          # Evaluate the expression
          result_value = evaluate_tree(tree)

          # Change result type from float to int if possible
          if isinstance(result_value, float) and result_value.is_integer():
            result_value = int(result_value)
        
        except Exception:
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

  return results


def output_results(results, output_path):

  with open(output_path, "w") as output_file:

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


def format_tokens(token_list):

    parts = []

    # Cycle through each token in the token list
    for token_type, token_value in token_list:
        if token_type == "END":
            parts.append(f"[{token_type}]")
        else:
            parts.append(f"[{token_type}:{token_value}]")
    return " ".join(parts)


def process_expression(expr):

  global tokens, pos
  
  tokens = tokenize(expr)
  pos = 0
  
  tree = parse_expression()
  
  if current_token()[0] != "END":
    raise ValueError()
  
  return tree

      
#Step 2: Tokenizer Converting string into tokens 
def tokenize(expr: str):

  tokens = []
  i = 0
  
  while i < len(expr):  
    ch = expr[i]
    
    if ch.isdigit():
      num = ch
      i += 1
      
      while i < len(expr) and expr[i].isdigit():  
        num += expr[i]
        i += 1
        
      tokens.append(("NUM", num))
      continue  
    
    elif ch in "+-*/":  
      tokens.append(("OP", ch))
    
    elif ch == "(":
      tokens.append(("LPAREN", ch))
      
    elif ch == ")":
      tokens.append(("RPAREN", ch))
      
    elif ch.isspace():  
      i += 1
      continue
      
    else:
      raise ValueError("Invalid character")  
      
    i += 1  
    
  tokens.append(("END", ""))
  return tokens


#Step 3: Recursive Descent Parser
def parse_expression():
  node = parse_term()

  while current_token()[1] in ("+", "-"):
    op = consume()[1]
    right = parse_term()
    node = (op, node, right)
    
  return node 

def parse_term():
  node = parse_factor()

  while current_token()[1] in ("*", "/"):
    op = consume()[1]
    right = parse_factor()
    node = (op, node, right)
    
  return node 

def parse_factor():
  token_type, token_value = current_token()

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
  return tokens[pos]

def consume():
  global pos
  token = tokens[pos]
  pos += 1
  return token

#Step 4: Parse Tree
def tree_to_string(node):
  if isinstance(node, float):
    return str(int(node)) if node.is_integer() else str(node)
    
  if node[0] == "neg":
    return f"(neg {tree_to_string(node[1])})"
    
  op, left, right = node
  return f"({op} {tree_to_string(left)} {tree_to_string(right)})"

#Step 5: Evaluate Tree
def evaluate_tree(input_tree):
  
  # For Debug
  #print(input_tree)
    
  if isinstance(input_tree, float):
    return input_tree
  
  if input_tree[0] == "neg":
    return -evaluate_tree(input_tree[1])

  left_value = evaluate_tree(input_tree[1])
  right_value = evaluate_tree(input_tree[2])


  if input_tree[0] == "+":
    return left_value + right_value
  
  elif input_tree[0] == "-":
    return left_value - right_value
  
  elif input_tree[0] == "*":
    return left_value * right_value
  
  elif input_tree[0] == "/":
    if right_value == 0:
      raise ValueError("Division by zero")
    return left_value / right_value

  else:
    raise ValueError("Invalid tree node")




results = evaluate_file("Q2/input.txt")
output_results(results, "Q2/output.txt")

  