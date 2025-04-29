grammar g;

IGNORE : ('program =: 3 : 0' | NEWLINE+ ')' | 'program ' '\'' '\'') -> skip ; // TODO

program: NEWLINE* statement+ EOF;

statement
    : expr endOfStmt                                # exprStmt
    | declaration endOfStmt                         # declarationStmt
    | IF expr DO
        NEWLINE* statement+ END endOfStmt           # ifStmt
    | WHILE expr DO 
        NEWLINE* statement+ END endOfStmt           # whileStmt
    | MAIN NEWLINE+ statement+ END endOfStmt        # mainCall
    | FUNCTION ID '(' (ID (';' ID)*)? ')' NEWLINE+
       statement+ END endOfStmt                     # funcStmt
    
    | RETURN expr? endOfStmt                        # returnStmt

    | WRITE STRING endOfStmt                        # writeStmt
    
    ;

endOfStmt
    : NEWLINE+ 
    | EOF
    ;

declaration: ID ASSIGN expr;

expr
    : '(' expr ')'                                  # parent
    
    | ID '(' (expr (';' expr)*)? ')'                # funcCall

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

WRITE: 'write' ;

MAIN: 'main' ;
FUNCTION: 'function' ;
RETURN: 'return' ;

IF: 'if.' ;
END: 'end.' ;
WHILE: 'while.' ;
DO: 'do.' ;

ASSIGN      : '=:' | '=.'; // TODO
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


