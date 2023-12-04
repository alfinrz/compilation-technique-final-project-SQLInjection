from ply import lex

# Define the token types
tokens = (
    'INTEGER',
    'PLUS',
    'MINUS',
)

# Define regular expressions for each token type
t_PLUS = r'\+'
t_MINUS = r'-'
t_ignore = ' \t\n'  # Ignore whitespace characters

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Example usage:
text = "12 + 34 - 5"

# Give the lexer some input
lexer.input(text)

# Tokenize the input
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)