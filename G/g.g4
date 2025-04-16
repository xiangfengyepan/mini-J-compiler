grammar g;

program: (statement NEWLINE*)* EOF;

statement
    : expr
    | declaration
    ;

declaration: ID ASSIGN expr;

expr
    : '(' expr ')'                                  # parent
    | ID                                            # variable
    | ID expr+                                      # funcCall

    | op=(IDENTITY|HASH|ARANGE) expr                # unary
    | op=(NEG|PLUS)  expr                           # unary

    | expr op=(CONCATE|HASH|INDEX) FLIP? expr       # aritmetic
    | expr op=(MUL|DIV|POW|MOD) FLIP? expr          # aritmetic
    | expr op=(PLUS|MINUS) FLIP? expr               # aritmetic

    | op=(CONCATED|HASHD|INDEXD) expr               # aritmetic
    | op=(MULD|DIVD|POWD|MODD) expr                 # aritmetic
    | op=(PLUSD|MINUSD) expr                        # aritmetic

    | op=(CONCATE|HASH|INDEX) FOLD expr             # fold
    | op=(MUL|DIV|POW|MOD) FOLD expr                # fold
    | op=(PLUS|MINUS) FOLD expr                     # fold

    | expr op=(EQUAL|NE|LT|GT|LE|GE) expr           # relational
    | INTVAL+                                       # value
    | INTVAL                                        # value
    // | FLOATVAL+                                  # value
    ;

ASSIGN      : '=:' ;
EQUAL       : '=' ;
NE          : '<>';
LT          : '<';
GT          : '>';
LE          : '<=';
GE          : '>=';

NEG         : '_';

PLUS        : '+' ;
MINUS       : '-';
MUL         : '*';
DIV         : '%';
POW         : '^';
MOD         : '|';
CONCATE     : ',';
HASH        : '#';
INDEX       : '{';

IDENTITY    : ']';
ARANGE      : 'i.';
FOLD        : '/'; 
FLIP        : '~';

PLUSD        : '+:';
MINUSD       : '-:';
MULD         : '*:';
DIVD         : '/:';
POWD         : '^:';
MODD         : '%:';
CONCATED     : ',:';
HASHD        : '#:';
INDEXD       : '@:';

INTVAL    : ('0'..'9')+ ;
// FLOATVAL  : ('0'..'9')+ '.' ('0'..'9')+ ;
ID        : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')* ;

// Strings (in quotes) with escape sequences
STRING    : '"' ( ESC_SEQ | ~('\\'|'"') )* '"' ;

fragment
ESC_SEQ   : '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\') ;

NEWLINE : '\r'? '\n' ;

COMMENT: 'NB.' ~[\r\n]* -> skip;

WS        : [ \t\r]+ -> skip ;    


