/* Problem 2: Java Lexer */
/* Ashok Vishwakarma, 180151 */
%{
    #include <iostream>
    #include <fstream> //used for file handling
    #include <string>
    #include <vector>
    #include <map>

    using namespace std; //using standard namespace
    // file pointer for input file
    extern FILE *yyin;
    // character pointer for yytext
    extern char *yytext;

    extern int yylex();

    enum Token_Type {
	    KEYWORD, IDENTIFIER, NUM_LITERAL, LITERAL, CHAR_LITERAL, STRING_LITERAL, PTR_LITERAL, OPERATOR, SERPERATOR
    };

    vector<string> token_names = {"Keyword", "Identifier", "NUM_LITERAL", "Literal", "CHAR_LITERAL", "STRING_LITERAL", "PTR_LITERAL", "Operator", "Seperator"};

    // list for token
    vector<string> list = {};

    // map for token
    map<string, string> token;
    // map for token count
    map<string, int> tokenCount;

%}

/* Digits*/
digit	    [0-9]
alpha	    [a-zA-Z_]
FL			(f|F|l|L)

%%
"abstract"        {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    } // Keywords in Java Language

"continue"        {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"for"             {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"new"             {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"switch"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"assert"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"default"         {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"if"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"package"         {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"synchronized"    {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"boolean"         {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"do"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"goto"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"private"         {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"this"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"break"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"double"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"implements"      {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"protected"       {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"throw"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"byte"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"else"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"import"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"public"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"throws"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"case"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"enum"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"instanceof"      {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"return"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"transient"       {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"catch"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"extends"         {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"int"             {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"short"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"try"             {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"char"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"final"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"interface"       {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"static"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"void"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"class"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"finally"         {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"long"            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"strictfp"        {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"volatile"        {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"const"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"float"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"native"          {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"super"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    }

"while"           {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    } // Keywords ends


"_"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[KEYWORD];
                        }
                    else tokenCount[str]++;
                    } // Underscore


"+"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                } // Operators begins

"-"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"*"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"/"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"&"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"|"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"^"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"%"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"="               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

">"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"<"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"!"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"~"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"?"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

":"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"->"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"=="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

">="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"<="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"!="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"&&"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"||"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"++"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"--"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"<<"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

">>"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

">>>"             {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"+="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"-="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"*="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"/="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"&="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"|="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"^="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"%="              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

"<<="             {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

">>="             {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                }

">>>="            {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[OPERATOR];
                    }
                    else tokenCount[str]++;
                } //Operator ends

"("               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                } //Seperator begins

")"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

"{"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

"}"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

"["               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

"]"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

";"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

","               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

"."               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

"..."             {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

"@"               {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                }

"::"              {char *str = yytext;
                    if(tokenCount.find(str)==tokenCount.end()){
                        list.push_back(str);
                        tokenCount[str] = 1;
                        token[str] = token_names[SERPERATOR];
                    }
                    else tokenCount[str]++;
                } // Seperator ends


"/*"              {int c;
                    while ((c = yyinput()) != EOF){
                        if (c == '*') {
                            while ((c = yyinput()) == '*');
                            if (c == '/') return 1;
                            if (c == -1) break;
                        }
                    }
                } // Multi Line Comment

"//"              {char c; int i= 0;
                    while ((c = yyinput()) != '\n' && c != 0) {i++;} 
                } // Single Line Comment

"'"                  {} // Ignore
"\""                 {} // Ignore

[ \t\v\n\f\0\b\s\r ] {return 0;} // Whitespaces

<<EOF>> {return -1;} /*End of file*/

{alpha}({alpha}|{digit})*           {char *str = yytext;
                                if(tokenCount.find(str)==tokenCount.end()){
                                    list.push_back(str);
                                    tokenCount[str] = 1;
                                    token[str] = token_names[IDENTIFIER];
                                    }
                                else tokenCount[str]++;
                            } // regex for Identifier

([+-])?{digit}+{FL}?        {char *str = yytext;
                                if(tokenCount.find(str)==tokenCount.end()){
                                    list.push_back(str);
                                    tokenCount[str] = 1;
                                    token[str] = token_names[LITERAL];
                                    }
                                else tokenCount[str]++;
                            } // regex for Literal

([+-])?{digit}+"."{digit}+{FL}? {char *str = yytext;
                                    if(tokenCount.find(str)==tokenCount.end()){
                                        list.push_back(str);
                                        tokenCount[str] = 1;
                                        token[str] = token_names[LITERAL];
                                        }
                                    else tokenCount[str]++;
                                }

alpha?\"(\\.|[^\\"])*\"	    {char *str = yytext;
                            if(tokenCount.find(str)==tokenCount.end()){
                                list.push_back(str);
                                tokenCount[str] = 1;
                                token[str] = token_names[LITERAL];
                                }
                            else tokenCount[str]++;
                        }
%%

int yywrap() { return 1;}

int main(int argc, char *argv[]){
    if(argc == 1){
        cout << "[Error] Input java file is missing as an argument!!" << endl;
        return -1;
    }
    else if(argc > 2){
        cout << "[Error] Too many arguments!!" << endl;
        return -1;
    }
    else{
        FILE *file;
        file = fopen(argv[1],"r");
        if (file == NULL) {
            cout << "The file " << argv[1] <<" could not be opened\n";
            exit(1);
        }
        yyin = file;
    }

    int op;

    while((op = yylex())!=-1);

    // Redirecting the output to csv file
    std::ofstream myfile;
    myfile.open ("problem2_output.csv");
    if (myfile.fail()) {
        cout << "Couldn't open the file!" << endl;
        return 0;
    }
    myfile << "Lexeme, Token, tokenCount" << endl;
    for(auto i:list){
        myfile << i << ", " << token[i] << ", " << tokenCount[i] << endl;
    } 
    myfile.close();

    return 0;
}