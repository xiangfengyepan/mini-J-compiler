grammar g;

program: (statement NEWLINE*)* EOF;

statement
    : expr
    | declaration
    ;

declaration: ID ASSIGN expr;

expr
    : '(' expr ')'                          # parent
    | ID                                    # variable
    | ID expr+                              # funcCall
    | op=(NEG|PLUS|NOT) expr                # unary
    | expr op=(MUL|DIV|POW|MOD) expr        # aritmetic
    | expr op=(PLUS|MINUS) expr             # aritmetic
    | expr op=(EQUAL|NE|LT|GT|LE|GE) expr  # relational
    | expr op=AND expr                      # logical
    | expr op=OR expr                       # logical
    | INTVAL+                               # value
    // | FLOATVAL+                             # value
    ;

ASSIGN      : '=:' ;
EQUAL       : '=' ;
NE          : '<>';
LT          : '<';
GT          : '>';
LE          : '<=';
GE          : '>=';

AND         : '&';
OR          : '/';
NOT         : '~';

NEG         : '_';
PLUS        : '+' ;
MINUS       : '-';
MUL         : '*';
DIV         : '%';
POW         : '^';
MOD         : '|';

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


