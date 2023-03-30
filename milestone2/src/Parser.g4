parser grammar Parser;

options {
    tokenVocab=Lexer;
}

//literals

literal
	:	IntegerLiteral
	|	FloatingPointLiteral
	|	BooleanLiteral
	|	CharacterLiteral
	|	StringLiteral
	|	NullLiteral
	;

//variables

type0
	:	typeName
	|	refType
	;

typeSpec
    :   classOrInterfaceType ('[' ']')*
    |   typeName ('[' ']')*
    ;
typeName
	:	 numerictypes
	|	 'boolean'
	;

numerictypes
	:	integertype
	|	floatingtype
	;

integertype
	:	'int'
	|	'long'
	;

floatingtype
	:	'float'
	|	'double'
	;

refType
	:	classOrInterfaceType
	|	typeVar
	|	arrayType
	;

classOrInterfaceType
	:	Identifier typeArgs? ( '.'  Identifier typeArgs? )*
	;

classType
	:	 Identifier typeArgs?
	|	classOrInterfaceType '.'  Identifier typeArgs?
	;

interfaceType
	:	classType
	;

typeVar
	:	 Identifier
	;

arrayType
	:	typeName dims
	|	classOrInterfaceType dims
	|	typeVar dims
	;

dims
	:	 '[' ']' ( '[' ']')*
	;

typeParam
	:	Identifier typeBound?
	;

typeBound
	:	'extends' typeVar
	|	'extends' classOrInterfaceType additionalBound*
	;

additionalBound
	:	'&' interfaceType
	;

typeArgs
	:	'<' typeArgList '>'
	;

typeArgList
	:	typeArg (',' typeArg)*
	;

typeArg
	:	refType
	;


//names

type_r
	:	Identifier
	|	packageOrTypeName '.' Identifier
	;

packageOrTypeName
	:	Identifier
	|	packageOrTypeName '.' Identifier
	;

expName
	:	Identifier
	|	ambiguousName '.' Identifier
	;

methodName
	:	Identifier
	;

packageName
	:	Identifier
	|	packageName '.' Identifier
	;

ambiguousName
	:	Identifier
	|	ambiguousName '.' Identifier
	;


//production

prog
	:	typeDeclaration* EOF
	;

typeDeclaration
	:	classDeclaration
	|	';'
	;

/*************Productions from §8 (Classes)*************/

classDeclaration
	:	normalClassDeclaration
	;

normalClassDeclaration
	:	classAccessModifier* 'class' Identifier typeParams? superclass? superinterfaces? classBody
	;

classAccessModifier
	:	'public'
	|	'private'
	|	'static'
	;

typeParams
	:	'<' typeParamList '>'
	;

typeParamList
	:	typeParam (',' typeParam)*
	;

superclass
	:	'extends' classType
	;

superinterfaces
	:	'implements' interfaceTypeList
	;

interfaceTypeList
	:	interfaceType (',' interfaceType)*
	;

classBody
	:	'{' classBodyDeclaration* '}'
	;

classBodyDeclaration
	:	classMembers
	|	instanceInit
	|	staticInit
	|	constructorDeclaration
	;

classMembers
	:	fieldDeclaration
	|	methodDeclaration
	|	classDeclaration
	|	';'
	;

fieldDeclaration
	:	fieldModifier* unannType varDeclaratorList ';'
	;

fieldModifier
	:	'public'
	|	'private'
	|	'static'
	;

varDeclaratorList
	:	varDeclarator (',' varDeclarator)*
	;

varDeclarator
	:	varDeclaratorId (op = '=' init)?
	;

varDeclaratorId
	:	Identifier dims?
	;

init
	:	expression
	|	arrayInit
	;

unannType
	:	unannPrimitiveType
	|	unannRefType
	;

unannPrimitiveType
	:	numerictypes
	|	'boolean'
	;

unannRefType
	:	unannClassOrInterfaceType
	|	unannTypeVar
	|	unannArrayType
	;

unannClassOrInterfaceType
	:	( Identifier typeArgs? ) ( '.'  Identifier typeArgs? )*
	;

unannClassType
	:	Identifier typeArgs?
	|	unannClassOrInterfaceType '.'  Identifier typeArgs?
	;

unannInterfaceType
	:	unannClassType
	;

unannTypeVar
	:	Identifier
	;

unannArrayType
	:	unannPrimitiveType dims
	|	unannClassOrInterfaceType dims
	|	unannTypeVar dims
	;

methodDeclaration
	:	methodAccessModifier* header method
	;

methodAccessModifier
	:	'public'
	|	'private'
	|	'static'
	;

header
	:	result methodDeclarator
	|	typeParams  result methodDeclarator
	;

result
	:	unannType
	|	'void'
	;

methodDeclarator
	:	Identifier '(' formalParamList? ')' dims?
	;

formalParamList
	:	receiverParam
	|	formalParams ',' lastFormalParam
	|	lastFormalParam
	;

formalParams
	:	formalParam (',' formalParam)*
	|	receiverParam (',' formalParam)*
	;

formalParam
	:	unannType varDeclaratorId
	;

lastFormalParam
	:	formalParam
	;

receiverParam
	:	 unannType (Identifier '.')? 'this'
	;


method
	:	block
	|	';'
	;

instanceInit
	:	block
	;

staticInit
	:	'static' block
	;

constructorDeclaration
	:	constructorModifier* constructorDeclarator constructorBody
	;

constructorModifier
	:	'public'
	|	'private'
	;

constructorDeclarator
	:	typeParams? simpleTypeName '(' formalParamList? ')'
	;

simpleTypeName
	:	Identifier
	;

constructorBody
	:	'{' explicitConstructorInvocation? blockStmts? '}'
	;

explicitConstructorInvocation
	:	typeArgs? 'this' '(' argList? ')' ';'
	|	typeArgs? 'super' '(' argList? ')' ';'
	|	expName '.' typeArgs? 'super' '(' argList? ')' ';'
	|	primary '.' typeArgs? 'super' '(' argList? ')' ';'
	;


//interfaces



interfaceModifier
	:	'public'
	|	'private'
	|	'static'
	;


constantDeclaration
	:	constantModifier* unannType varDeclaratorList ';'
	;

constantModifier
	:	'public'
	|	'static'
	;

defaultValue
	:	'default' elementValue
	;


elementValuePairList
	:	elementValuePair (',' elementValuePair)*
	;

elementValuePair
	:	Identifier '=' elementValue
	;

elementValue
	:	condExp
	|	elementValueArrayInit
	;

elementValueArrayInit
	:	'{' elementValueList? ','? '}'
	;

elementValueList
	:	elementValue (',' elementValue)*
	;


//arrays

arrayInit
	:	'{' initList? ','? '}'
	;

initList
	:	init (',' init)*
	;


//blocks

block
	:	'{' blockStmts? '}'
	;

blockStmts
	:	blockStmt blockStmt*
	;

blockStmt
	:	localVarDeclarationStmt
	|	classDeclaration
	|	stmt
	;

localVarDeclarationStmt
	:	localVarDeclaration ';'
	;

localVarDeclaration
	:	unannType varDeclaratorList
	;

stmt
	:	stmtNoTrailing
	|	labeledStmt
	|	ifStmt
	|	ifElseStmt
	|	whileLoop
	|	forLoop
	;

stmtNoShortIf
	:	stmtNoTrailing
	|	labeledStmtNoShortIf
	|	ifElseStmtNoShortIf
	|	whileStmtNoShortIf
	|	forStmtNoShortIf
	;

stmtNoTrailing
	:	block
	|	emptyStmt
	|	expressionStmt
	|	returnStmt
	;

emptyStmt
	:	';'
	;

labeledStmt
	:	Identifier ':' stmt
	;

labeledStmtNoShortIf
	:	Identifier ':' stmtNoShortIf
	;

expressionStmt
	:	stmtExp ';'
	;

stmtExp
	:	assign
	|	preIncExp
	|	preDecExp
	|	postIncExp
	|	postDecExp
	|	invocMethod
	|	classCreation
	;

ifStmt
	:	'if' cond =  '(' expression ')' body = stmt
	;

ifElseStmt
	:	'if' cond =  '(' expression ')' stmtNoShortIf 'else' body = stmt
	;

ifElseStmtNoShortIf
	:	'if' cond =  '(' expression ')' stmtNoShortIf 'else' body = stmtNoShortIf
	;


whileLoop
	:	'while' cond =  '(' expression ')' body = stmt
	;

whileStmtNoShortIf
	:	'while' cond = '(' expression ')' body = stmtNoShortIf
	;


forLoop
	:	basicForStmt
	|	enhancedForStmt
	;

forStmtNoShortIf
	:	basicForStmtNoShortIf
	|	enhancedForStmtNoShortIf
	;

basicForStmt
	:	'for' cond = '(' forInit? ';' expression? ';' forUpdate? ')' body = stmt
	;

basicForStmtNoShortIf
	:	'for' cond = '(' forInit? ';' expression? ';' forUpdate? ')' body = stmtNoShortIf
	;

forInit
	:	stmtExpList
	|	localVarDeclaration
	;

forUpdate
	:	stmtExpList
	;

stmtExpList
	:	stmtExp (',' stmtExp)*
	;

enhancedForStmt
	:	'for' cond = '(' unannType varDeclaratorId ':' expression ')' body = stmt
	;

enhancedForStmtNoShortIf
	:	'for' cond = '(' unannType varDeclaratorId ':' expression ')' body = stmtNoShortIf
	;



returnStmt
	:	'return' expression? ';'
	;

resourceSpec
	:	'(' resourceList ';'? ')'
	;

resourceList
	:	resource (';' resource)*
	;

resource
	:	unannType varDeclaratorId '=' expression
	;


//expressions

primary
	:	( primaryNoNewArray0 | arrayCreationExp ) ( primaryNoNewArray1 )*
	;

primaryNoNewArray
	:	literal
	|	type_r ('[' ']')* '.' 'class'
	|	'void' '.' 'class'
	|	'this'
	|	type_r '.' 'this'
	|	'(' expression ')'
	|	classCreation
	|	field
	|	array
	|	invocMethod
	|	methodRef
	;

primaryNoNewArray2
	:	literal
	|	type_r ('[' ']')* '.' 'class'
	|	'void' '.' 'class'
	|	'this'
	|	type_r '.' 'this'
	|	'(' expression ')'
	|	classCreation
	|	field
	|	invocMethod
	|	methodRef
	;

primaryNoNewArray1
	:	classCreation0
	|	field0
	|	array0
	|	invocMethod0
	|	methodRef0
	;

primaryNoNewArray3
	:	classCreation0
	|	field0
	|	invocMethod0
	|	methodRef0
	;

primaryNoNewArray0
	:	literal
	|	type_r ('[' ']')* '.' 'class'
	|	unannPrimitiveType ('[' ']')* '.' 'class'
	|	'void' '.' 'class'
	|	'this'
	|	type_r '.' 'this'
	|	'(' expression ')'
	|	classCreation1
	|	field1
	|	array1
	|	invocMethod1
	|	methodRef1
	;

primaryNoNewArray4
	:	literal
	|	type_r ('[' ']')* '.' 'class'
	|	unannPrimitiveType ('[' ']')* '.' 'class'
	|	'void' '.' 'class'
	|	'this'
	|	type_r '.' 'this'
	|	'(' expression ')'
	|	classCreation1
	|	field1
	|	invocMethod1
	|	methodRef1
	;

classCreation
	:	unqualifiedClassCreation
	|	expName '.' unqualifiedClassCreation
	|	primary '.' unqualifiedClassCreation
	;

unqualifiedClassCreation
    :   'new' typeArgs? classOrInterfaceTypeToInstantiate '(' argList? ')' classBody?
    ;

classOrInterfaceTypeToInstantiate
    :    Identifier ('.'  Identifier)* typeArgsOrDiamond?
    ;

classCreation0
	:	'.' 'new' typeArgs?  Identifier typeArgsOrDiamond? '(' argList? ')' classBody?
	;

classCreation1
	:	'new' typeArgs?  Identifier ('.'  Identifier)* typeArgsOrDiamond? '(' argList? ')' classBody?
	|	expName '.' 'new' typeArgs?  Identifier typeArgsOrDiamond? '(' argList? ')' classBody?
	;

typeArgsOrDiamond
	:	typeArgs
	|	'<' '>'
	;

field
	:	primary '.' Identifier
	|	'super' '.' Identifier
	|	type_r '.' 'super' '.' Identifier
	;

field0
	:	'.' Identifier
	;

field1
	:	'super' '.' Identifier
	|	type_r '.' 'super' '.' Identifier
	;

array
	:	( expName '[' expression ']' |	primaryNoNewArray2 '[' expression ']' )	( '[' expression ']' )*
	;

array0
	:	( primaryNoNewArray3 '[' expression ']' ) ( '[' expression ']' )*
	;

array1
	:	( expName '[' expression ']' |	primaryNoNewArray4 '[' expression ']' ) ( '[' expression ']' )*
	;

invocMethod
	:	methodName '(' argList? ')'
	|	type_r '.' typeArgs? Identifier '(' argList? ')'
	|	expName '.' typeArgs? Identifier '(' argList? ')'
	|	primary '.' typeArgs? Identifier '(' argList? ')'
	|	'super' '.' typeArgs? Identifier '(' argList? ')'
	|	type_r '.' 'super' '.' typeArgs? Identifier '(' argList? ')'
	;

invocMethod0
	:	'.' typeArgs? Identifier '(' argList? ')'
	;

invocMethod1
	:	methodName '(' argList? ')'
	|	type_r '.' typeArgs? Identifier '(' argList? ')'
	|	expName '.' typeArgs? Identifier '(' argList? ')'
	|	'super' '.' typeArgs? Identifier '(' argList? ')'
	|	type_r '.' 'super' '.' typeArgs? Identifier '(' argList? ')'
	;

argList
	:	expression (',' expression)*
	;

methodRef
	:	expName '::' typeArgs? Identifier
	|	refType '::' typeArgs? Identifier
	|	primary '::' typeArgs? Identifier
	|	'super' '::' typeArgs? Identifier
	|	type_r '.' 'super' '::' typeArgs? Identifier
	|	classType '::' typeArgs? 'new'
	|	arrayType '::' 'new'
	;

methodRef0
	:	'::' typeArgs? Identifier
	;

methodRef1
	:	expName '::' typeArgs? Identifier
	|	refType '::' typeArgs? Identifier
	|	'super' '::' typeArgs? Identifier
	|	type_r '.' 'super' '::' typeArgs? Identifier
	|	classType '::' typeArgs? 'new'
	|	arrayType '::' 'new'
	;

arrayCreationExp
	:	'new' typeName dimExprs dims?
	|	'new' classOrInterfaceType dimExprs dims?
	|	'new' typeName dims arrayInit
	|	'new' classOrInterfaceType dims arrayInit
	;

dimExprs
	:	dimExpr dimExpr*
	;

dimExpr
	:	 '[' expression ']'
	;

expression
	:	assignExp
	;

inferredFormalParamList
	:	Identifier (',' Identifier)*
	;

assignExp
	:	condExp
	|	assign
	;

assign
	:	leftHandSide assignOp expression
	;

leftHandSide
	:	expName
	|	field
	|	array
	;

assignOp
	:	'='
	|	'*='
	|	'/='
	|	'%='
	|	'+='
	|	'-='
	|	'<<'
	|	'>>'
	|	'>>>'
	|	'&='
	|	'^='
	|	'|='
	;

condExp
	:	condOrExp
	|	condOrExp '?' expression ':' condExp
	;

condOrExp
	:	condAndExp
	|	left = condOrExp op = '||' right = condAndExp
	;

condAndExp
	:	inOrExp
	|	left = condAndExp op = '&&' right = inOrExp
	;

inOrExp
	:	exOrExp
	|	left = inOrExp op = '|' right = exOrExp
	;

exOrExp
	:	andExp
	|	left = exOrExp op = '^' right = andExp
	;

andExp
	:	eqExp
	|	left = andExp op = '&' right = eqExp
	;

eqExp
	:	relation
	|	left = eqExp op = '==' right = relation
	|	left = eqExp op = '!=' right = relation
	;

relation
	:	shiftExp
	|	left = relation op = '>' right = shiftExp
	|	left = relation op = '<' right = shiftExp
	|	left = relation op = '>=' right = shiftExp
	|	left = relation op = '<=' right = shiftExp
	;

shiftExp
	:	addExp
	|	left = shiftExp op = '<<' right = addExp
	|	left = shiftExp op = '>>' right = addExp
	|	left = shiftExp op = '>>>' right = addExp
	;

addExp
	:	multiplyExp
	|	left = addExp op = '+' right = multiplyExp
	|	left = addExp op = '-' right = multiplyExp
	;

multiplyExp
	:	unaryExp
	|	left = multiplyExp op = '*' right = unaryExp
	|	left = multiplyExp op = '/' right = unaryExp
	|	left = multiplyExp op = '%' right = unaryExp
	;

unaryExp
	:	preIncExp
	|	preDecExp
	|	'+' unaryExp
	|	'-' unaryExp
	|	unaryExpNotPlusMinus
	;

preIncExp
	:	'++' unaryExp
	;

preDecExp
	:	'--' unaryExp
	;

unaryExpNotPlusMinus
	:	postfixExp
	|	'~' unaryExp
	|	'!' unaryExp
	|	castExp
	;

postfixExp
	:	( primary | expName ) ( '++' | '--' )*
	;

postIncExp
	:	postfixExp '++'
	;

postDecExp
	:	postfixExp '--'
	;

castExp
	:	'(' typeName ')' unaryExp
	|	'(' refType additionalBound* ')' unaryExpNotPlusMinus
	;

constantExp
	:	expression
	;