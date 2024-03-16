import ply.lex as lex

# List of token names
tokens = (
    'START',
    'END',
    'MOVE',
    'ROTATE',
    'DEPTH',
    'NUMBER',
)

# Regular expression rules for tokens
t_START = r'start'
t_END = r'end'
t_MOVE = r'move'
t_ROTATE = r'rotate'
t_DEPTH = r'depth'
t_NUMBER = r'[0-9]+'

# Ignored characters (whitespace)
t_ignore = ' \t\r\n'





