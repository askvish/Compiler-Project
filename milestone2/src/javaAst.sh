#!/bin/bash

if [[ $1  == "-input" && $3 == "" ]];then
	cat $2 | python AST.py "ast.dot" 1>/dev/null
	# echo "hi"
elif [[ $1 == "-input" && $3 == "-output" ]];then 1>/dev/null
	cat $2 | python AST.py $4
elif [[ $1 == "-help" ]];then
	echo "Abstract Syntax Tree (in DOT format) for the given input Java program"
elif [[ $1 == "-verbose" ]];then
	echo "Use -input flag  to run the executable, to give the input file"
	echo "Provide -out for output file.otherwise the output would be created at ast.dot"
	echo "Use -help for help"
	echo "The final execution procedure should be ./javaAst -input in.java [-output output]"

fi
