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

unaryOperators
    : //(POWD|MULD|PLUSD|MINUSD|
    (IDENTITY|HASH|ARANGE|
        NEG|PLUS)                   # unaryOp
    | (MUL|DIV|POW|MOD|
            PLUS|MINUS) FOLD        # foldOp
;

binaryOperators:
    (CONCATE|HASH|INDEX|
            PLUS|MINUS|MUL|DIV|POW|MOD
            |EQUAL|NE|LT|GT|LE|GE) FLIP?    # binaryOp
;

expr
    : '(' expr ')'                                  # parent
    | op=(IDENTITY|HASH|ARANGE|
        NEG|PLUS) expr                              # unary

    | <assoc=right> expr 
        op=(CONCATE|HASH|INDEX|
        PLUS|MINUS|MUL|DIV|POW|MOD
        |EQUAL|NE|LT|GT|LE|GE) FLIP? expr           # aritmetic

    | op=(POW|MOD|PLUS|MINUS) DOUBLE expr           # aritmetic

    | op=(CONCATE|
        MUL|DIV|POW|MOD|
        PLUS|MINUS) FOLD expr                       # fold

    | INTVAL+                                       # value
    | ID                                            # variable
    // | op=( IDENTITY|HASH|ARANGE|
    //         NEG|PLUS|ID) expr?                      # unaryFuncCall                                     
    // | expr op=( IDENTITY|HASH|ARANGE|
    //         NEG|PLUS|ID) expr                       # binaryFuncCall     
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

// PLUSD        : '+:' ;
// MINUSD       : '-:' ;
// MULD         : '*:' ;
// POWD         : '^:' ;
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


