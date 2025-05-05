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

declaration
    : ID ASSIGN expr                                # exprDeclaration
    | ID ASSIGN composeOperators                    # operatorDeclaration
    ;

composeOperators
    : simpleOperators+ (COMPOSE simpleOperators+)*
    ;

simpleOperators
    : unaryOperators
    | binaryOperators
    | foldOperators                   
    | expr
    ;

unaryOperators
    : (MULD|PLUSD|
        IDENTITY|HASH|ARANGE|
        NEG)    
    ;              
foldOperators
    : (MUL|DIV|POW|MOD|
        PLUS|MINUS) FOLD
    ;

binaryOperators
    : (CONCATE|HASH|INDEX|
        PLUS|MINUS|MUL|DIV|POW|MOD|
        EQUAL|NE|LT|GT|LE|GE) FLIP?
    ;

expr
    : '(' expr ')'                                  # parent

    | <assoc=right> expr binaryOperators expr       # binaryAritmetic

    | unaryOperators expr                           # unaryAritmetic

    | foldOperators expr                            # foldAritmetic

    | PLUS? INTVAL+                                 # value
    | ID                                            # variable

    | ID expr                                       # unaryFuncCall  

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

PLUSD       : '+:' ;
MULD        : '*:' ;

COMPOSE     : '@:' ;

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


