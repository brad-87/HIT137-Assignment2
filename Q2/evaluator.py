#Step 1: Read input file
def evaluate_file(input_path: str):
  with open(input_path, "r") as file:
    lines = file.readlines()
  
  for line in lines:
    print(line.strip())

#Step 2: Tokenizer Converting string into tokens 
def tokenize(expr: str):
  tokens = []
  i = 0
  
  while i < len(expr):  ?
    ch = expr[i]
    
    if ch.isdigit():
      num = ch
      i += 1
      
      while i < len(expr) and expr[i].isdigit():  ?
        num += expr[i]
        i += 1
        
      tokens.append(("NUM", num))
      continue  ?
    
    elif ch in "+-*/":  ?
      tokens.append(("OP", ch))
    
    elif ch == "(":
      tokens.append(("LPAREN", ch))
      
    elif ch == ")":
      tokens.append(("RPAREN", ch))
      
    elif ch.isspace():  ?
      pass
      
    else:
      raise ValueError("Invalid character")  ?
      
    i += 1  ?
    
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
  tok_type, tok_value = current_token()

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

def current_tokens():
  return token[pos]

def consume():
  global pos
  tok = tokens[pos]
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
    
                       
                  
      

            
    

  






    
