grammar g;

program: NEWLINE* statements EOF;

statements: statement+ ;

statement
    : expr endOfStmt                                # exprStmt
    | declaration endOfStmt                         # declarationStmt
    ;


endOfStmt
    : NEWLINE+ 
    | EOF
    ;

declaration: ID ASSIGN expr;

expr
    : '(' expr ')'                                  # parent

    | op=(IDENTITY|HASH|ARANGE) expr                # unary
    | op=(NEG|PLUS)  expr                           # unary

    | <assoc=right> expr 
        op=(CONCATE|HASH|INDEX) FLIP? expr          # aritmetic
    | <assoc=right> expr 
        op=(PLUS|MINUS|MUL|DIV|POW|MOD) FLIP? expr  # aritmetic

    | op=(CONCATE|HASH|INDEX) DOUBLE expr           # aritmetic
    | op=(MUL|DIV|POW|MOD) DOUBLE expr              # aritmetic
    | op=(PLUS|MINUS) DOUBLE expr                   # aritmetic

    | op=(CONCATE|HASH|INDEX) FOLD expr             # fold
    | op=(MUL|DIV|POW|MOD) FOLD expr                # fold
    | op=(PLUS|MINUS) FOLD expr                     # fold

    | <assoc=right> 
        expr op=(EQUAL|NE|LT|GT|LE|GE) expr         # relational
    | INTVAL+                                       # value
    | ID                                            # variable
    ;

ASSIGN      : '=:';
EQUAL       : '=' ;
NE          : '<>' ;
LT          : '<' ;
GT          : '>' ;
LE          : '<=' ;
GE          : '>=' ;

NEG         : '_' ;

PLUS        : '+' ;
MINUS       : '-' ;
MUL         : '*' ;
DIV         : '%' ;
POW         : '^' ;
MOD         : '|' ;
CONCATE     : ',' ;
HASH        : '#' ;
INDEX       : '{' ;

IDENTITY    : ']' ;
ARANGE      : 'i.' ;
FOLD        : '/' ; 
FLIP        : '~' ;

DOUBLE      : ':' ;

INTVAL    : ('0'..'9')+ ;
ID        : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;

// Strings (in quotes) with escape sequences
STRING    : '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

fragment
ESC_SEQ   : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;

NEWLINE : '\r'? '\n' ;

COMMENT: 'NB.' ~[\r\n]* -> skip ;

WS        : [ \t\r]+ -> skip ;   

LEXICAL_ERROR: . ;


