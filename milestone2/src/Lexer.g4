lexer grammar Lexer;

//keywords

BOOLEAN : 'boolean';
BREAK : 'break';
BYTE : 'byte';
CASE : 'case';
CATCH : 'catch';
CHAR : 'char';
CLASS : 'class';
CONST : 'const';
CONTINUE : 'continue';
DEFAULT : 'default';
DO : 'do';
DOUBLE : 'double';
ELSE : 'else';
ENUM : 'enum';
EXTENDS : 'extends';
FINAL : 'final';
FINALLY : 'finally';
FLOAT : 'float';
FOR : 'for';
IF : 'if';
IMPLEMENTS : 'implements';
INT : 'int';
INTERFACE : 'interface';
LONG : 'long';
NATIVE : 'native';
NEW : 'new';
PRIVATE : 'private';
PUBLIC : 'public';
RETURN : 'return';
SHORT : 'short';
STATIC : 'static';
SUPER : 'super';
SWITCH : 'switch';
THIS : 'this';
VOID : 'void';
WHILE : 'while';



//interger literals

IntegerLiteral
	:	DecimalInt
	|	HexInt
	|	OctalInt
	|	BinaryInt
	;

fragment
DecimalInt
	:	Decimal [lL]?
	;

fragment
HexInt
	:	Hex [lL]?
	;

fragment
OctalInt
	:	OctalNumeral [lL]?
	;

fragment
BinaryInt
	:	Binary [lL]?
	;

fragment
Decimal
	:	'0'
	|	[1-9] Digits?
    |   [1-9] Underscores Digits
	;

fragment
Digits
	:	Digit 
    |   Digit DigitsAndUnderscores? Digit
	;

fragment
Digit
	:	'0'
	|	[1-9]
	;

fragment
DigitsAndUnderscores
	:	DigitOrUnderscore+
	;

fragment
DigitOrUnderscore
	:	Digit
	|	'_'
	;

fragment
Underscores
	:	'_'+
	;

fragment
Hex
	:	'0' [xX] HexDigits
	;

fragment
HexDigits
	:	[0-9a-fA-F]
    |   [0-9a-fA-F] HexDigitsAndUnderscores? [0-9a-fA-F]
	;


fragment
HexDigitsAndUnderscores
	:	HexDigitOrUnderscore+
	;

fragment
HexDigitOrUnderscore
	:	[0-9a-fA-F]
	|	'_'
	;

fragment
OctalNumeral
	:	'0' OctalDigits
    |   '0' Underscores OctalDigits
	;

fragment
OctalDigits
	:	[0-7]
    |   [0-7] OctalDigitsAndUnderscores? [0-7]
	;

fragment
OctalDigitsAndUnderscores
	:	OctalDigitOrUnderscore+
	;

fragment
OctalDigitOrUnderscore
	:	[0-7]
	|	'_'
	;

fragment
Binary
	:	'0' [bB] BinaryDigits
	;

fragment
BinaryDigits
	:	[01]
    |   [01] BinaryDigitsAndUnderscores? [01]
	;

fragment
BinaryDigitsAndUnderscores
	:	BinaryDigitOrUnderscore+
	;

fragment
BinaryDigitOrUnderscore
	:	[01]
	|	'_'
	;


// Float Literals

FloatingPointLiteral
	:	DecimalFloatingPointLiteral
	|	HexadecimalFloatingPointLiteral
	;

fragment
DecimalFloatingPointLiteral
	:	Digits '.' Digits? ExponentPart? [fFdD]?
	|	'.' Digits ExponentPart? [fFdD]?
	|	Digits ExponentPart [fFdD]?
	|	Digits ExponentPart? [fFdD]
	;

fragment
ExponentPart
	:	[eE] SignedInteger
	;

fragment
SignedInteger
	:	[+-]? Digits
	;

fragment
HexadecimalFloatingPointLiteral
	:	HexSignificand BinaryExponent [fFdD]?
	;

fragment
HexSignificand
	:	Hex '.'?
	|	'0' [xX] HexDigits? '.' HexDigits
	;

fragment
BinaryExponent
	:	[pP] SignedInteger
	;


//boolean literals

BooleanLiteral
	:	'true'
	|	'false'
	;


//char literals

CharacterLiteral
	:	'\'' ~['\\\r\n] '\''
	|	'\'' EscapeSequence '\''
	;


/***************3.10.5 String Literals***************/

StringLiteral
	:	'"' StringCharacter* '"'
	;

fragment
StringCharacter
	:	~["\\\r\n]
	|	EscapeSequence
	;


//escape sequence

fragment
EscapeSequence
	:	'\\' [btnfr"'\\]
	|	OctalEscape
    ;

fragment
OctalEscape
	:	'\\' [0-7]
	|	'\\' [0-7] [0-7]
	|	'\\' ZeroToThree [0-7] [0-7]
	;

fragment
ZeroToThree
	:	[0-3]
	;


//null

NullLiteral
	:	'null'
	;


//seperators

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMICOLON : ';';
COMMA : ',';
DOT : '.';
DCOLON : '::';


//operators

ASSIGN : '=';
GT : '>';
LT : '<';
EXCLAMATION : '!';
TILDE : '~';
QUESTIONMARK : '?';
COLON : ':';
ARROW : '->';
EQUAL : '==';
GE : '>=';
LE : '<=';
NOTEQUAL : '!=';
AND : '&&';
OR : '||';
INC : '++';
DEC : '--';
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
BITAND : '&';
BITOR : '|';
CARET : '^';
MOD : '%';
LSHIFT : '<<';
RSHIFT : '>>';
URSHIFT : '>>>';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MUL_ASSIGN : '*=';
DIV_ASSIGN : '/=';
AND_ASSIGN : '&=';
OR_ASSIGN : '|=';
XOR_ASSIGN : '^=';
MOD_ASSIGN : '%=';



//identifiers

Identifier
	:	IdentifierChars
	;

fragment
IdentifierChars
    :   [a-zA-Z$_] [a-zA-Z0-9$_]*
    ;


//whitespaces

WS  :  [ \t\r\n]+ -> skip
    ;

MULTI_LINE_COMMENT
    :   '/*' .*? '*/' -> skip
    ;

SINGLE_LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;