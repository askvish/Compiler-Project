#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Compiler Project - CS335A
Milestone 3
Ashok Vishwakarma | 180151
Viraj | 180870

"""


import ply.lex as lex
from ply.lex import TOKEN
import sys

# different types of tokens
tokens = (
    'Keyword',
    'Identifier',
    'FloatingLiteral',
    'IntegerLiteral',
    'BooleanLiteral',
    'CharacterLiteral',
    'StringLiteral',
    'Separator',
    'Comments',
    'Operator',
    'OP_DIM'
)

# Regular expression rules for simple tokens
Alphabets = r'([a-zA-Z])'
Numeric = r'([0-9])'
Alphanum = r'([a-zA-Z0-9])'
IdentifierStart = r'([0-9a-zA-Z$_])'

# regrex for identifier
Identifier = r'[a-zA-Z$_][a-zA-Z0-9$_]*'

# regex for reserved keywords
Keyword = r'(continue|for|new|switch|assert|default|goto|boolean|do|if|finally|final|private|this|class|break|double|protected|byte|else|import|public|case|enum|return|catch|extends|int|short|try|char|static|void|long|volatile|const|float|String|while|interfaces|throw|throws)' + \
    r'[^0-9a-zA-Z$_]'
# not matches like forLoop, ifStmt, ...

# regrex for interger point literal
IntegerLiteral = r'[0-9]+'

# regrex for floating point literal
FloatingLiteral = r'(([0-9]+)?\.([0-9]+)((e|E)((\+|-)?[0-9]+))?([fFdD])?|[0-9]+(e|E)(\+|-)?[0-9]+)'

# regrex for boolean literal
BooleanLiteral = r'(true|false|TRUE|FALSE)'


# regex for special characters: \ ! % ^ & $ * () - + = { } | ~ [ \; : < > ? , . / # @ ` _ ]
Special = r'([\]!%\^&$*()-+={}|~[\;:<>?,./#@`_])'

# Graphic pattern matches any character that is either alphanumeric or a special character in Special pattern.
Graphic = r'([a-zA-Z0-9]|' + Special + r')'


# regrex for character literal which matches a character literal such as 'a', '7', '\n', '\'', etc.
CharacterLiteral = r'(\'(' + Graphic + r'|\ |\\[n\\ta"\'])\')'

# regrex for string literal which matches a string literal such as "Hello, world!", "abc123", "line1\nline2", "\"quoted string\" is fun", etc.
StringLiteral = r'(\"(' + Graphic + r'|\ |\\[n\\ta"\'])*\")'

# regrex for illegal identifiers like 2hello
Illegals = r'('+IntegerLiteral + r'[a-zA-Z]+)'

OP_DIM = r'\[[\t ]*\]'

# regrex for separators
Separator = r'[;,.(){}[\] \"\']'

# regrex for operators
Operator = r'(>>>=|<<=|>>=|<<|>>|>>>|<=|>=|<|>|\+\+[^+=]|--[^\-=]|[+\-*/%&\^|]=|\+[^+=]|-[^\-=]|\*|/|==|=|~|!=|%|instanceof|!|&&|\^|\|\||&|\|)'

# regrex for both single line and multiline comments
Comments = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'

# A regular expression rule with some action code


@TOKEN(Comments)
def t_Comments(t):
    t.lexer.lineno += t.value.count('\n')
    pass


@TOKEN(Illegals)
def t_Illegals(t):
    print("Line :: %d  Illegal entry '%s'" % (t.lexer.lineno, t.value))
    pass


@TOKEN(Keyword)
def t_Keyword(t):
    t.type = keywords[t.value[:-1]]
    t.lexer.lexpos -= 1
    v = t.value[:-1]
    t.value = v
    return t


ReservedWords = ["TRUE", "true", "FALSE", "false", "null"]


@TOKEN(Identifier)
def t_Identifier(t):
    if (t.value in ReservedWords):
        t.type = "BooleanLiteral"
    return t


@TOKEN(FloatingLiteral)
def t_FloatingLiteral(t):
    return t


@TOKEN(IntegerLiteral)
def t_IntegerLiteral(t):
    return t


@TOKEN(BooleanLiteral)
def t_BooleanLiteral(t):
    return t


@TOKEN(CharacterLiteral)
def t_CharacterLiteral(t):
    return t


@TOKEN(StringLiteral)
def t_StringLiteral(t):
    return t


@TOKEN(OP_DIM)
def t_OP_DIM(t):
    return t


@TOKEN(Separator)
def t_Separator(t):
    t.type = separators[t.value]
    return t


@TOKEN(Operator)
def t_Operator(t):
    # print("\t\t-->", t)
    # print("\t\t-->", t.value[:-1], "||", t.value[-1])
    cond1 = t.value[:-1] == '+' or t.value[:-
                                           1] == '-' or t.value[:-1] == '++' or t.value[:-1] == '--'
    # print("\t\tcond1-->", cond1)
    # print("\t\tcond2-->", t.value[-1] != '=')
    # print("\t\tcond1 and cond2-->", cond1 and t.value[-1] != '=')
    if (cond1 and t.value[-1] != '='):
        # print("\t\tt.value-->", t.value)
        t.value = t.value[:-1]
        # print("\t\tt.value-->", t.value)
        t.lexer.lexpos = t.lexer.lexpos-1
    t.type = operators[t.value]
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_error(t):
    print("Line :: %d  Illegal entry '%s'" % (t.lexer.lineno, t.value))
    t.lexer.skip(1)


keyw = ['continue', 'for', 'new', 'switch', 'assert', 'default', 'goto', 'boolean', 'final', 'do', 'if', 'private', 'this', 'break', 'double', 'protected', 'byte', 'else', 'import', 'public', 'case',
        'enum', 'return', 'catch', 'extends', 'int', 'short', 'try', 'char', 'static', 'void', 'class', 'long', 'volatile', 'const', 'finally', 'float', 'String', 'while', 'interfaces', 'throw', 'throws']

keywords = {}
for i in keyw:
    keywords[i] = "KEY" + str(i).upper()
tokens = tokens + tuple(keywords.values())

operators = {
    '+':    'PLUS',
    '-':    'MINUS',
    '*':    'MULTIPLY',
    '/':    'DIVIDE',
    '%':    'MOD',
    '=':    'EQUAL',
    '<=':   'LESSEQ',
    '>=':   'GREATEQ',
    '<':    'LESSER',
    '>':    'GREATER',
    '==':   'CHECKEQ',
    '++':   'INCREMENT',
    '--':   'DECREMENT',
    '~':   'TILDE',
    '!':   'NOT',
    '<<':   'LEFTSHIFT',
    '>>':   'RIGHTSHIFT',
    '>>>':  'LOGICALSHIFT',
    'instanceof':   'INSTANCEOF',
    '!=':   'NOTEQ',
    '&':   'BINAND',
    '^':   'XOR',
    '|':   'BINOR',
    '?':   'TERNARY',
    '&&':  'AND',
    '||':  'OR',
    '+=':  'PLUSEQ',
    '/=':  'DIVIDEEQ',
    '-=':  'MINUSEQ',
    '*=':  'MULTIPLYEQ',
    '%=':  'MODEQ',
    '&=':  'BINANDEQ',
    '^=':  'XOREQ',
    '|=':  'BINOREQ',
    '<<=': 'LEFTSHIFTEQ',
    '>>=': 'RIGHTSHIFTEQ',
    '>>>=': 'LOGICALSHIFTEQ'

}
for i in operators:
    operators[i] = "OP" + operators[i]
tokens = tokens + tuple(operators.values())

separators = {
    ';': 'SEMICOLON',
    ',': 'COMMA',
    '.': 'DOT',
    '(': 'LEFTBRACE',
    ')': 'RIGHTBRACE',
    '{': 'LEFTPARAN',
    '}': 'RIGHTPARAN',
    '[': 'LEFTSQBR',
    ']': 'RIGHTSQBR',
    '"': 'DOUBLEINCO',
    '\'': 'SINGLEINCO',
    ':': 'COLON'
}

for i in separators:
    separators[i] = "SEP" + separators[i]
tokens = tokens + tuple(separators.values())

# build the lexer
lexer = lex.lex()

# main function


def main():
    print("Lexical Analyzer:")

    filename = sys.argv[1]
    f = open(filename, 'r')
    data = f.read()

    f.close()

    lexer.input(data)

    for tok in lexer:
        print(tok)


if __name__ == '__main__':
    main()
